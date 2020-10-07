
import config
from pages.templates.elements import *



class HomePage:

    def __init__(self, driver):

        driver.get(config.coinbase_home_url)
        self.page = driver

    # NAVIGATION BAR

    home_link_loc = (by.XPATH, "//a[@title='Home']")
    prices_link_loc = (by.XPATH, "//a[@title='Prices']")
    products_menu_loc = (by.XPATH, "//button[contains(text(),'Products')]")
    company_menu_loc = (by.XPATH, "//button[contains(text(),'Company')]")
    earn_crypto_link_loc = (by.XPATH, "//a[@title='Earn Crypto']")

    def home_link(self): return Link(self.page, self.home_link_loc)
    def prices_link(self): return Link(self.page, self.prices_link_loc)













