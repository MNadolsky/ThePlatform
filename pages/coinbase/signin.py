
import config
import secure.cookies
from pages.templates.elements import *



class SigninPage:

    def __init__(self, driver, drivethrough=True, inject_cookies=True):

        # sign in page title: Coinbase - Buy/Sell Digital Currency
        if not drivethrough: driver.get(config.coinbase_domain + '/signin')
        if inject_cookies:
            for cookie in secure.cookies.coinbase: 
                driver.add_cookie(cookie)

        self.driver = driver

        self.build_elements()


    # NAVIGATION BAR

    home_link_loc =     (by.CLASS_NAME, 'Header__Logo')
    products_menu_loc = (by.LINK_TEXT, 'Products')
    help_link_loc =     (by.LINK_TEXT, 'Help')
    prices_link_loc =   (by.LINK_TEXT, 'Prices')
    sign_in_link_loc =  (by.LINK_TEXT, 'Sign In')
    sign_up_button_loc =(by.LINK_TEXT, 'Sign Up')

    # BODY

    email_field_loc =               (by.ID, 'email')
    pass_field_loc =                (by.ID, 'password')
    stay_signed_in_checkbox_loc =   (by.ID, 'stay_signed_in')
    sign_in_button_loc =            (by.ID, 'signin_button')
    forgot_password_link_loc =      (by.LINK_TEXT, 'Forgot password?')
    no_account_link_loc =           (by.LINK_TEXT, "Don't have an account?")
    privacy_policy_link_loc =       (by.LINK_TEXT, 'Privacy Policy')
    two_factor_link_loc = \
        (by.LINK_TEXT, 'Have an issue with 2-factor authentication?')

    def build_elements(self):

        # NAVIGATION BAR

        self.home_link =      Link(self.driver, self.home_link_loc)
        self.products_menu =  ReactiveMenu(self.driver, self.products_menu_loc)
        self.help_link =      Link(self.driver, self.help_link_loc)
        self.prices_link =    Link(self.driver, self.prices_link_loc)
        self.sign_in_link =   Link(self.driver, self.sign_in_link_loc)
        self.sign_up_button = Button(self.driver, self.sign_up_button_loc)
        
        # BODY

        self.email_field = Field(self.driver, self.email_field_loc)
        self.pass_field = Field(self.driver, self.pass_field_loc)
        self.stay_signed_in_checkbox = ''
        self.sign_in_button = Button(self.driver, self.sign_in_button_loc)
        self.forgot_password_link = ''
        self.no_account_link = ''
        self.privacy_policy_link = ''
        self.two_factor_link =''       










    
