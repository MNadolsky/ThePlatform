
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import sys

import pages.destinations



class Element:
    """
    This is the template base class. It contains all functionality common to all
    templates - namely driver handling, locator specification, and element
    finding. This class takes a driver and a locator and provides a function for
    retrieving the element associated with that locator

    Inputs
    -----
    driver: selenium driver pointed at the url containing the element
    locator: selenium locator that uniquely describes the element
    """

    def __init__(self, driver, locator):

        self.driver = driver
        self.locator = locator

    def element(self):

        wait(self.driver,10).until(
            EC.visibility_of_element_located(self.locator))
        return self.driver.find_element(*self.locator)

    def exists(self):

        try: self.element()
        except: return False
        return True



class Button(Element):
    """
    Inputs:
    -----
    wait_for: selenium locator
              Sometimes when a button is clicked javascript processes are kicked
              off and selenium doesn't wait for them to finish, continuing on
              with the next line before the "click" is finished. wait_for
              specifies an element that must be visible before the click() will
              exit.
    destination: string
                 For use, see pages.destinations documentation
    """

    def __init__(self, driver, locator, wait_for=None, destination=None):

        super().__init__(driver, locator)
        self.wait_locator = wait_for
        self.destination = destination

    def click(self):

        wait(self.driver,10).until(EC.element_to_be_clickable(self.locator))
        self.element().click()
        if self.wait_locator: wait(self.driver,10).until(
            EC.visibility_of_element_located(self.wait_locator))

        if self.destination:
            return pages.destinations.get_page(self.driver, self.destination)


class Link(Element):
    """
    Inputs:
    -----
    destination: string
                 For use, see pages.destinations documentation
    """
    def __init__(self, driver, locator, destination=None):

        super().__init__(driver, locator)
        self.destination = destination

    def click(self):

        wait(self.driver,10).until(EC.element_to_be_clickable(self.locator))
        self.element().click()

        if self.destination:
            return pages.destinations.get_page(self.driver, self.destination)



class Field(Element):

    def click(self): self.element().click()
    def input(self, keys): self.element().send_keys(keys)
    def clear(self): self.element().clear()
    

class ReactiveMenu(Element):
    """
    This class is an attempt to capture the functionality of a general class of
    non-standard menus and dropdowns. It provides a method to open a menu and
    click on an item.

    Inputs
    -----
    wrapper_locator: selenium locator for a parent element of the menu items
        If a menu wrapper locator is not specified, only basic functionality is
        available. Passing the locator enables selection by index and more
        accurate selection by text.
    """

    def __init__(self, driver, locator, wrapper_locator=None):

        super().__init__(driver, locator)
        self.wrapper_loc = wrapper_locator 

    def wrapper(self):
        """
        Find and return the element that contains the menu items)
        """
        wait(self.driver,10).until(
            EC.presence_of_element_located(self.wrapper_loc))
        return self.driver.find_element(*self.wrapper_loc)

    def open(self):
        """
        Open the menu without selecting an item.
        Note: Do not use open() before using select(). See the note in select().
        """

        self.element().click()

    def select(self, item_selector):
        """
        Note: Do not use open() before using select(). select() calls open(),
        which can cause an error if the open menu obscures the menu trigger
        button.

        Inputs
        -----
        item_selector: str (or int, if wrapper_locator was passed to __init__())
            The exact text of the menu item to be selected is to be passed as a
            str. if wrapper_locator was passed on instantiation an int can be
            passed to select by index (1-indexed).
        """

        self.element().click()

        if self.wrapper_loc:

            if type(item_selector) is int:

                item_loc = (by.XPATH, './/a')
                items = self.wrapper().find_elements(*item_loc)
                item = items[item_selector - 1]

            elif type(item_selector) is str:

                item_loc = (by.XPATH, f".//*[.='{item_selector}']")
                item = self.wrapper().find_element(*item_loc)

        else:

            # Alternate method included in case it turns out to be better
            #item_loc = (by.XPATH, f"//*[normalize-space()='{item_selector}']")
            item_loc = (by.XPATH, f"//*[.='{item_selector}']")
            item = self.driver.find_element(*item_loc)

        if item.tag_name is not 'a': 

            parent = item.find_element_by_xpath('..')            
            if parent is 'a': item = parent

        item.click()

