
import config
from pages.templates.elements import *



class DashboardPage:

    def __init__(self, driver, drivethrough=True):

        if not drivethrough: driver.get(config.coinbase_domain + '/dashboard')
        self.driver = driver

        self.build_elements()



    # NAVIGATION BAR

    logo_link_loc = (by.XPATH, "//*[contains(@class,'StyledLogo')]")
    home_link_loc = (by.LINK_TEXT, 'Home')
    portfolio_link_loc = (by.LINK_TEXT, 'Portfolio')
    prices_link_loc = (by.LINK_TEXT, 'Prices')
    earn_rewards_link_loc = (by.XPATH, '//a[@href="/rewards"]')
    trade_button_loc = (by.XPATH, '//button[.="Trade"]')
    send_button_loc = (by.XPATH, '//button[.="Send"]')
    receive_button_loc = (by.XPATH, '//button[.="Receive"]')

    # ReactiveMenu needs to be modified to work with these
    #notifications_menu_loc = (by.XPATH, "//*[contains(@class,'Bell__Icon')]")
    #avatar_menu_loc = (by.XPATH, "//*[contains(@class,'Avatar__')]")

    def build_elements(self):

        # NAVIGATION BAR

        self.logo_link = Link(self.driver, self.logo_link_loc)
        self.home_link = Link(self.driver, self.home_link_loc)
        self.portfolio_link = Link(self.driver, self.portfolio_link_loc)
        self.prices_link = Link(self.driver, self.prices_link_loc)
        self.earn_rewards_link = Link(self.driver, self.earn_rewards_link_loc)
        self.trade_button = Button(self.driver, self.trade_button_loc)
        self.send_button = Button(self.driver, self.send_button_loc)
        self.receive_button = Button(self.driver, self.receive_button_loc)
        #self.notifications_menu = 
        #self.avatar_menu = 






