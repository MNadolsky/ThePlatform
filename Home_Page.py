from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

import Secure 
import config



class Home_Page():

    def __init__(self,driver):
        self.driver = driver
        driver.get(config.homepage_url)

    #Buttons

    # coinbase has two-factor authentication which involves sending a text
    # via cellphone; it is optional to forego this authentication, so 
    # cookies are added below to do this. It is currently unclear which cookie controls 
    # the authentication. So, I just signed in, checked the option to not ask for
    # the text code again, then signed out and grabbed all the cookies. Below I loaded 
    # all these cookies which include the cookie/s necessary to forego this second 
    # authentication.


    def click_home_page_sign_in_button(self):
        home_page_sign_in_button_loc = (By.XPATH,"//a[@title='Sign in']")
        wait(self.driver,15).until(EC.element_to_be_clickable(home_page_sign_in_button_loc))
        self.driver.find_element(*home_page_sign_in_button_loc).click()
        for cookie in Secure.cookies_coinbase: self.driver.add_cookie(cookie)
