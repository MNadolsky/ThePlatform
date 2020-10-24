
import config
import secure.creds
import secure.cookies
from pages.templates.elements import *



class SigninPage:

    def __init__(self, driver, spawn=False, bypass_auth=True):
        """
        inputs
        -----
        driver = selenium driver
        spawn: bool
            The default use case is that a driver that is already at the 
            appropriate url is passed in as part of a user workflow. if 
            spawn=True, the driver will be navigated to the appropriate url on 
            instantiation.
        bypass_auth: bool
            Two-factor authentication is manditory. When bypass_auth is true,
            cookies for the option to bypass are added before login. The cookie
            file is in /secure and not tracked, so one must be built according
            to README.md.
            If bypass_auth is False, the login process will require two-factor
            auth.
        """

        # sign in page title: Coinbase - Buy/Sell Digital Currency
        if spawn: driver.get(config.coinbase_domain + '/signin')
        if bypass_auth:
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

    email_field_loc =                  (by.ID, 'email')
    pass_field_loc =                   (by.ID, 'password')
    keep_me_signed_in_checkbox_loc =   (by.ID, 'stay_signed_in')
    sign_in_button_loc =               (by.ID, 'signin_button')
    forgot_password_link_loc =         (by.LINK_TEXT, 'Forgot password?')
    not_have_account_link_loc =        (by.LINK_TEXT, "Don't have an account?")
    privacy_policy_link_loc =          (by.PARTIAL_LINK_TEXT, 'Privacy Policy')
    two_factor_link_loc = (
        by.LINK_TEXT, 'Have an issue with 2-factor authentication?')

    # MISC

    sign_in_error_alert_loc = (by.LINK_TEXT, 'Invalid email or password.')

    def build_elements(self):

        # NAVIGATION BAR

        self.home_link =      Link(self.driver, self.home_link_loc)
        self.products_menu =  ReactiveMenu(self.driver, self.products_menu_loc)
        self.help_link =      Link(self.driver, self.help_link_loc)
        self.prices_link =    Link(self.driver, self.prices_link_loc)
        self.sign_in_link =   Link(self.driver, self.sign_in_link_loc)
        self.sign_up_button = Button(self.driver, self.sign_up_button_loc)
        
        # BODY

        self.email_field =         Field(self.driver, self.email_field_loc)
        self.pass_field =          Field(self.driver, self.pass_field_loc)
        self.keep_me_signed_in_checkbox = CheckBox(
                              self.driver, self.keep_me_signed_in_checkbox_loc)
        self.sign_in_button =      Button(self.driver, self.sign_in_button_loc)
        self.forgot_password_link = Link(
                                    self.driver, self.forgot_password_link_loc)
        self.not_have_account_link = Link(
                                    self.driver,self.not_have_account_link_loc)
        self.privacy_policy_link = Link(
                                      self.driver,self.privacy_policy_link_loc)
        self.two_factor_link =     Link(self.driver,self.two_factor_link_loc)       

        # MISC

        # This element only appears after an errant login attempt; it is the 
        # error message popup
        self.sign_in_error_alert = Element(
            self.driver, self.sign_in_error_alert_loc)

    # WORKFLOWS 

    def login(self, bypass_auth=True):
        """
        The normal user login flow beginning from /signin

        inputs
        -----
        bypass_auth: bool       #Should this docString be near the __init__ method? since bypas_auth is first given there
            Two-factor authentication is manditory. When bypass_auth is true,
            cookies for the option to bypass are added before login. The cookie
            file is in /secure and not tracked, so one must be built:
            1. Log in manually, choosing the option to skip two-factor auth next
               time
            2. Log out
            3. Do driver.get_cookies and print the results (it's a list)
            4. Make a file called cookies in /secure, declare a single variable
               called coinbase, and copy and paste the cookie list into the variable
            5. Delete any newlines in the middle of the dictionary keys/values

            If bypass_auth is False, the login process will require two-factor
            auth.
        """

        if bypass_auth:
            #self.driver.delete_all_cookies()
            for cookie in secure.cookies.coinbase:self.driver.add_cookie(cookie)

        self.email_field.input(secure.creds.CBuser)
        self.pass_field.input(secure.creds.CBpass)
        self.sign_in_button.click()
        

















    
