
import unittest

from selenium import webdriver

import config
import secure.creds
from pages.coinbase.homepage import HomePage
from pages.coinbase.signin import SigninPage
from pages.coinbase.dashboard import DashboardPage


class Login(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(config.chromedriver_path)
        self.page = SigninPage(driver, drivethrough=False)

    def runTest(self):

        page = self.page

        page.email_field.input(secure.creds.CBuser)
        page.pass_field.input(secure.creds.CBpass)
        page.sign_in_button.click()

        self.assertEqual \
            (page.driver.current_url, config.coinbase_domain + '/dashboard')
        self.assertEqual \
            (page.driver.title, 'Coinbase')

    def tearDown(self):

        self.page.driver.quit()



class Logout(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(config.chromedriver_path)
        page = SigninPage(driver, drivethrough=False)
        page.login()
        self.page = DashboardPage(driver)

    def runTest(self):

        self.page.avatar_menu.select('Sign out')

        self.assertEqual \
            (self.driver.title, 'Coinbase - Buy/Sell Digital Currency')
        self.assertEqual \
            (self.driver.current_url, config.coinbase_domain + 'signin') 

    def tearDown(self):

        self.page.driver.quit() 







if __name__ == '__main__': unittest.main()
