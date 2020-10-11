
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import sys


class Element:

    def __init__(self, driver, locator):

        self.driver = driver
        self.locator = locator
        #self.element = self.element()

    def element(self):

        wait(self.driver,10).until(EC.visibility_of_element_located(self.locator))
        return self.driver.find_element(*self.locator)



class Button(Element):

    def __init__(self, driver, locator, wait_for=None):

        super().__init__(driver, locator)
        self.wait_locator = wait_for

    def click(self):

        wait(self.driver,10).until(EC.element_to_be_clickable(self.locator))
        self.element().click()
        if self.wait_locator: wait(self.driver,10).until(EC.visibility_of_element_located(self.wait_locator))



class Link(Element):

    def click(self):

        wait(self.driver,10).until(EC.element_to_be_clickable(self.locator))
        self.element().click()



class Field(Element):

    def click(self): self.element().click()
    def input(self, keys): self.element().send_keys(keys)
    def clear(self): self.element().clear()



class ReactiveMenu(Element):

    def __init__(self, driver, locator, wrapper_locator=None):

        super().__init__(driver, locator)
        self.wrapper_loc = wrapper_locator 

    def wrapper(self):

        wait(self.driver,10).until(EC.presence_of_element_located(self.wrapper_loc))
        return self.driver.find_element(*self.wrapper_loc)

    def open(self):

        self.element().click()

    def select(self, item_selector):
        """
        Can select by using the text of the item or the index
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


            












