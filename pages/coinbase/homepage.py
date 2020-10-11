
import config
from pages.templates.elements import *



class HomePage:

    def __init__(self, driver):

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

        self.home_link =        Link(self.driver, self.home_link_loc)
        self.prices_link =      Link(self.driver, self.prices_link_loc)
        self.products_menu =    ReactiveMenu(self.driver,self.products_menu_loc)
        self.company_menu =     ReactiveMenu(self.driver, self.company_menu_loc)
        self.earn_crypto_link = Link(self.driver, self.earn_crypto_link_loc)
        self.sign_in_link =     Link(self.driver, self.sign_in_link_loc)
        self.header_get_started_button = Button(
            self.driver, self.header_get_started_button_loc)








