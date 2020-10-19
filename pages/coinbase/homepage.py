
import config
from pages.templates.elements import *



class HomePage:

    def __init__(self, driver, spawn=True):
        """
        inputs
        -----
        driver = selenium driver
        spawn: bool
            The default use case is that the driver being passed in is new and 
            needs to be navigated to the homepage. if spawn=False, it is assumed
            that the driver passed in is already at the homepage.
        """

        driver.get(config.coinbase_domain)
        self.driver = driver

        self.build_elements()

    # NAVIGATION BAR

    home_link_loc =         (by.XPATH, "//a[@title='Home']")
    prices_link_loc =       (by.XPATH, "//a[@title='Prices']")
    products_menu_loc =     (by.XPATH, "//button[contains(text(),'Products')]")
    company_menu_loc =      (by.XPATH, "//button[contains(text(),'Company')]")
    earn_crypto_link_loc =  (by.XPATH, "//a[@title='Earn crypto']")
    sign_in_link_loc =      (by.XPATH, "//a[@title='Sign in']")
    header_get_started_button_loc =(
        by.XPATH, "//a[.='Get started']")

    def build_elements(self):

        # NAVIGATION BAR

        self.home_link = Link(
            self.driver, self.home_link_loc, destination='home')
        self.prices_link = Link(self.driver, self.prices_link_loc)
        self.products_menu = ReactiveMenu(self.driver,self.products_menu_loc)
        self.company_menu = ReactiveMenu(self.driver, self.company_menu_loc)
        self.earn_crypto_link = Link(self.driver, self.earn_crypto_link_loc)
        self.sign_in_link = Link(
            self.driver, self.sign_in_link_loc, destination='signin')
        self.header_get_started_button = Button(
            self.driver, self.header_get_started_button_loc)







