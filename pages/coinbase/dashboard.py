
import config
from pages.templates.elements import *



class DashboardPage:

    def __init__(self, driver, drivethrough=True):

        if not drivethrough: 

            driver.get(config.coinbase_domain + '/dashboard')
            # handle redirect
            try: wait(driver,2).until(EC.url_contains('/signin'))
            except: pass

            if config.coinbase_domain + '/signin' in driver.current_url:
                # When pages reference other pages it is often circular, so the
                # import is done here to limit the defect potential
                from pages.coinbase.signin import SigninPage
                page = SigninPage(driver)
                page.login()

        self.driver = driver

        self.build_elements()



    # NAVIGATION BAR

    logo_link_loc =         (by.XPATH, "//*[contains(@class,'StyledLogo')]")
    home_link_loc =         (by.LINK_TEXT, 'Home')
    portfolio_link_loc =    (by.LINK_TEXT, 'Portfolio')
    prices_link_loc =       (by.LINK_TEXT, 'Prices')
    earn_rewards_link_loc = (by.XPATH, '//a[@href="/rewards"]')
    trade_button_loc =      (by.XPATH, '//button[.="Trade"]')
    send_button_loc =       (by.XPATH, '//button[.="Send"]')
    receive_button_loc =    (by.XPATH, '//button[.="Receive"]')
    notifications_menu_loc =(by.XPATH, "//*[contains(@class,'Bell__Icon')]")
    notifications_menu_wrapper_loc = (
        by.XPATH, "//div[contains(@class,'NotificationsEntry__Panel')]")
    avatar_menu_loc =       (by.XPATH, "//*[contains(@class,'Avatar__')]")
    avatar_menu_wrapper_loc = (
        by.XPATH, "//div[contains(@class,'DropdownMenu__Wrapper')]")

    settings_item_loc = (by.LINK_TEXT, 'Settings')
    taxes_and_reports_item_loc = (by.LINK_TEXT, 'Taxes & Reports')
    help_item_loc = (by.LINK_TEXT, 'Help')
    sign_out_item_loc = (by.LINK_TEXT, 'Sign out')

    def build_elements(self):

        # NAVIGATION BAR

        self.logo_link = Link(
            self.driver, self.logo_link_loc, destination='dashboard')
        self.home_link = Link(
            self.driver, self.home_link_loc, destination='dashboard')
        self.portfolio_link = Link(self.driver, self.portfolio_link_loc)
        self.prices_link = Link(self.driver, self.prices_link_loc)
        self.earn_rewards_link = Link(self.driver, self.earn_rewards_link_loc)
        self.trade_button = Button(self.driver, self.trade_button_loc)
        self.send_button = Button(self.driver, self.send_button_loc)
        self.receive_button = Button(self.driver, self.receive_button_loc)
        self.notifications_menu = ReactiveMenu(
            self.driver, self.notifications_menu_loc, 
            self.notifications_menu_wrapper_loc)
        self.avatar_menu = ReactiveMenu(
            self.driver, self.avatar_menu_loc, self.avatar_menu_wrapper_loc)

        self.settings_item = Link(self.driver, self.settings_item_loc)
        self.taxes_and_reports_item = Link(
            self.driver, self.taxes_and_reports_item_loc)
        self.help_item = Link(self.driver, self.help_item_loc)
        self.sign_out_item = Link(
            self.driver, self.sign_out_item_loc, destination='signin')

        

    # WORKFLOWS

    def logout(self):
        """
        Normal user logout flow
        """
        self.avatar_menu.open()
        signin_page = self.sign_out_item.click()

        return signin_page
        








