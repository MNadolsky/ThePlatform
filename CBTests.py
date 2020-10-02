
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import config
import secure.creds
import secure.cookies

import time



homepage_url = 'https://www.coinbase.com'

class Login(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome(config.chromedriver_path)
        self.driver.get(homepage_url + '/signin')

        # coinbase has two-factor authentification which involves sending a text
        # via cellphone; it is optional to forego this authentification, so 
        # cookies are added to do so.it is as yet unclear which cookie controls 
        # the authentication, so I just signed in with that option, signed out, 
        # grabbed all the cookes and dumped them in a file every cookie that 
        # would be present on signout is simply added to the new session 
        for cookie in cookies.coinbase: self.driver.add_cookie(cookie)

    def runTest(self):

        email_field = self.driver.find_element_by_id('email')
        pass_field = self.driver.find_element_by_id('password')
        sign_in_button = self.driver.find_element_by_id('signin_button')

        email_field.send_keys(secure.CBuser)
        pass_field.send_keys(secure.CBpass)
        sign_in_button.click()

        self.assertEqual(self.driver.current_url, homepage_url + '/dashboard')

    def tearDown(self):

        self.driver.close()



if __name__ == '__main__': unittest.main()
