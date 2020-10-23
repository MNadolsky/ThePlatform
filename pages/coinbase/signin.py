
import config
import secure.creds
import secure.cookies
from pages.templates.elements import *



class SigninPage:

    def __init__(self, driver, drivethrough=False, bypass_auth=True):

        # sign in page title: Coinbase - Buy/Sell Digital Currency
        if drivethrough: driver.get(config.coinbase_domain + '/signin')
        if bypass_auth:
            #driver.delete_all_cookies()
            for cookie in {'domain': '.coinbase.com', 'expiry': 1609521930, 'httpOnly': False, 'name': '_fbp', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fb.1.1601745930650.1822416352'}, {'domain': '.coinbase.com', 'expiry': 1601747727, 'httpOnly': True, 'name': '__cf_bm', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'dda8dc4da8eaa0d05eddb5bae8f7315696d3fd6e-1601745927-1800-AeOEbjEWSwHLHtfGjxoUeth7o29rdSjkrx2uy7hhySze5mZPlzzXRGu8eChC0cMhRFtLJc8Yj+fU7EZ8zKFqCtw='}, {'domain': '.coinbase.com', 'expiry': 1604337927, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'dd1f9520cad1eb878b80452ccb8f7374e1601745927'}, {'domain': 'www.coinbase.com', 'httpOnly': True, 'name': '_coinbase_session', 'path': '/', 'secure': True, 'value': 'VkF3WWhCUFBVZ1ROZjBvc3hLWHZoM0lHZm1RKzd3a0F1WkdzRjJ5c21ucWpEQmYxNnp5Y05ZZUNwMEJ2RklaaDY5Y3NEMS9RcDZuVWZLclcyWWhEU0x4TXFPU2VkcUZrNG9YdTk3WmY1VVF3ay9zSHJBZksvVHJEOVl1Qm5ZN2x1V3V0NnRCbkEyVFpFdExjNWJCU0ZLaFJmYmgya0JITWdmOUNocWdCSTVNPS0tdjhoKzFmd1AwVVlnVTJWc2lJSHdIUT09--e5f45123508a2aab0670f34fd272213e64630e22'}, {'domain': '.coinbase.com', 'expiry': 1664817930, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.953334938.1601745930'}, {'domain': 'www.coinbase.com', 'httpOnly': False, 'name': '_coinbase_strict', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': '0'}, {'domain': 'www.coinbase.com', 'httpOnly': False, 'name': '_coinbase_lax', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '0'}, {'domain': '.coinbase.com', 'expiry': 1601745990, 'httpOnly': False, 'name': '_gat_UA-32804181-23', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.coinbase.com', 'expiry': 1604341516, 'httpOnly': False, 'name': 'sft', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': '102c5cee4cef64f3fd32e8f877c40479'}, {'domain': 'www.coinbase.com', 'expiry': 1601832302, 'httpOnly': False, 'name': 'ba', 'path': '/', 'secure': True, 'value': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F85.0.4183.121%20Safari%2F537.36%23Win32%238%2320030107%23%23en-US%7C360%23300%23Wed%20Dec%2031%201969%2018%3A00%3A00%20GMT-0600%20(Central%20Standard%20Time)%2312%2F31%2F1969%2C%206%3A00%3A00%20PM%7C1920%231080%231920%231040%231%2324%2316%2388%7C9cea303ba0c125f44251aaa5b51f6f09%23f1dd45e1a64843ad5eb6380a4442271c%2393c0894315e92c6b4f9dbcc02e78237e%7C%7CAAAAAAAAAgAAAAACAABAAAAAAAABAICAAA%3D%3D'}, {'domain': 'www.coinbase.com', 'expiry': 10241659502, 'httpOnly': False, 'name': 'df2', 'path': '/', 'secure': True, 'value': '8c1b012dec4e39a359defe85c26e9be8'}, {'domain': 'www.coinbase.com', 'expiry': 10241659502, 'httpOnly': False, 'name': 'df', 'path': '/', 'secure': True, 'value': 'b1efdd863caff13c316485b924e31ef0'}, {'domain': '.coinbase.com', 'expiry': 1601832330, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1946295709.1601745930'}, {'domain': '.coinbase.com', 'expiry': 1917105900, 'httpOnly': False, 'name': 'coinbase_device_id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1b3bd3f7-47ef-4452-83d4-1e6c63425292'}: 
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
    privacy_policy_link_loc =       (by.PARTIAL_LINK_TEXT, 'Privacy Policy')
    two_factor_link_loc = (
        by.LINK_TEXT, 'Have an issue with 2-factor authentication?')

    # MISC

    #sign_in_error_alert_loc = (by.LINK_TEXT, 'Invalid email or password.')
    sign_in_error_alert_loc = (by.CLASS_NAME, 'alert')

    def build_elements(self):

        # NAVIGATION BAR

        self.home_link =      Link(self.driver, self.home_link_loc)
        self.products_menu =  ReactiveMenu(self.driver, self.products_menu_loc)
        self.help_link =      Link(self.driver, self.help_link_loc)
        self.prices_link =    Link(self.driver, self.prices_link_loc)
        self.sign_in_link =   Link(self.driver, self.sign_in_link_loc)
        self.sign_up_button = Button(self.driver, self.sign_up_button_loc)
        
        # BODY

        self.email_field =          Field(self.driver, self.email_field_loc)
        self.pass_field =           Field(self.driver, self.pass_field_loc)
        self.stay_signed_in_checkbox = ''
        self.sign_in_button =       Button(self.driver, self.sign_in_button_loc)
        self.forgot_password_link = ''
        self.no_account_link = ''
        self.privacy_policy_link = ''
        self.two_factor_link =''       

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
        bypass_auth: bool
            Two-factor authentication is manditory. When bypass_auth is true,
            cookies for the option to bypass are added before login. The cookie
            file is in /secure and not tracked, so one must be built:
            1. Log in manually, choosing the option to skip two-factor auth next
               time
            2. Log out
            3. Do driver.get_cookies and print the results (it's a list)
            4. Make a file in /secure, declare a single variable, and copy and
               paste the cookie list into the variable
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
        

















    
