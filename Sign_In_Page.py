from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import Secure 
import config
import time


class Sign_In_Page():

    def __init__(self,driver):
        self.driver = driver
        driver.get(config.signInPage_url)
    

    def click_sign_in_button(self):
        for cookie in Secure.cookies_coinbase: self.driver.add_cookie(cookie)
        self.driver.find_element_by_id('signin_button').click()

    def email_field(self): return self.driver.find_element_by_id('email')
    def input_email_field(self): self.email_field().send_keys(Secure.email)

    def password_field(self): return self.driver.find_element_by_id('password')
    def input_password(self): self.password_field().send_keys(Secure.password)