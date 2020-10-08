from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import secure.cookies
import secure.creds
import config
import time


class Sign_In_Page():

    def __init__(self,driver, get_SignIn_url: bool=None):  #if the driver is starting at the sign in page use keyword argument True at instantiation 
        self.driver = driver
        if get_SignIn_url: driver.get(config.coinbase_homepage_url+'/signin')

    def email_field_loc(self): return (By.ID,'email')
    def email_field(self): return self.driver.find_element(*self.email_field_loc()) 
    def input_email_field(self): self.email_field().send_keys(secure.creds.email)

    def password_field_loc(self): return (By.ID,'password')
    def password_field(self): return self.driver.find_element(*self.password_field_loc())
    def input_password(self): self.password_field().send_keys(secure.creds.password)

    def sign_in_button_loc(self): return (By.ID,'signin_button')
    def click_sign_in_button(self):
        for cookie in secure.cookies.coinbase: self.driver.add_cookie(cookie)
        self.driver.find_element(*self.sign_in_button_loc()).click()