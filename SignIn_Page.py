from selenium import webdriver
import Secure 
import config
from Home_Page import *


class SignIn_Page():
    driver = webdriver.Chrome(config.chromedriver_path,options=options)
    home_page = Home_Page(driver) 

    #Work Flow for Sign_In

    home_page.click_home_page_sign_in_button()
    home_page.email_field()
    home_page.input_email_field()
    home_page.password_field()
    home_page.input_password()
    home_page.click_sign_in_button()

