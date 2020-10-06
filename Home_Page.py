from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support import expected_conditions as EC   #these imports will be used in the future
#from selenium.webdriver.support.ui import WebDriverWait as wait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import Secure 
import config
import time
from Tools import *

options = Options()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging']) #this ignores DevTools that appear on the output 
options.add_argument('disable-gpu')


class Home_Page():

    def __init__(self,driver):
        self.driver = driver
        driver.get(config.homepage_url)

    #Buttons

    # coinbase has two-factor authentification which involves sending a text
    # via cellphone; it is optional to forego this authentification, so 
    # cookies are added below to do this. It is, as yet, unclear which cookie controls 
    # the authentication. So I just signed in, choosed the option to not ask for
    # the code again, then signed out and grabbed all the cookies. Below I loaded 
    # all these cookies which include the cookie/s necessary to forego this second 
    # authentification.

    def click_home_page_sign_in_button(self):
        self.driver.find_element_by_xpath("//a[@title='Sign in']").click()
        for cookie in Secure.cookies_coinbase: self.driver.add_cookie(cookie)

    def click_sign_in_button(self):
        self.driver.find_element_by_id('signin_button').click()
    
    #Fields

    def email_field(self): return self.driver.find_element_by_id('email')
    def input_email_field(self): self.email_field().send_keys(Secure.email)

    def password_field(self): return self.driver.find_element_by_id('password')
    def input_password(self): self.password_field().send_keys(Secure.password)

    #Drop Downs

    def click_profile_icon(self): self.driver.find_element_by_xpath("//span[@data-synthetic-id='user_menu_dropdown']").click()

    def click_sign_out_option(self): self.driver.find_element_by_xpath("//span[@data-synthetic-id='signout-menu-link']").click()

    