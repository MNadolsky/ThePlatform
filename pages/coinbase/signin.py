from selenium import webdriver
from selenium.webdriver.common.by import By
import secure.cookies
import secure.creds
#import secure      #I tried this and it didn't work with the code below, I also created a secure_test directory holding cred.py and cookies.py and that didn't work 
import config


class Sign_In_Page():

    def __init__(self,driver, bool=None):  #if the driver is starting at the sign in page use keyword argument True at instantiation 
        self.driver = driver
        if bool: driver.get(config.coinbase_homepage_url+'/signin')
        for cookie in secure.cookies.coinbase: self.driver.add_cookie(cookie)
    
    # coinbase has two-factor authentication which involves sending a text
    # via cellphone; it is optional to forego this authentication, so 
    # cookies are added above to do this. It is currently unclear which cookie controls 
    # the authentication. So, I just signed in, checked the option to not ask for
    # the text code again, then signed out and grabbed all the cookies. Above I loaded 
    # all these cookies which include the cookie/s necessary to forego this second 
    # authentication.  I can probably shorten this explanation.

    #Sign in locators

    email_field_loc = (By.ID,'email')
    password_field_loc = (By.ID,'password')
    sign_in_button_loc = (By.ID,'signin_button')

    #Sign in 

    def email_field(self): return self.driver.find_element(*self.email_field_loc) 
    def email_field_input(self): self.email_field().send_keys(secure.creds.email)

    def password_field(self): return self.driver.find_element(*self.password_field_loc)
    def password_field_input(self): self.password_field().send_keys(secure.creds.password)

    def sign_in_button_click(self): self.driver.find_element(*self.sign_in_button_loc).click()