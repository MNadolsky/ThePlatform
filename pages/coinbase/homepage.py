from selenium import webdriver
from selenium.webdriver.common.by import By
import secure.cookies
import config


#sign_in_button_loc = (By.XPATH,"//a[@title='Sign in']")

class Home_Page():

    def __init__(self,driver):
        self.driver = driver
        driver.get(config.coinbase_homepage_url)

    sign_in_button_loc = (By.XPATH,"//a[@title='Sign in']")
    def click_home_page_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button_loc).click()

