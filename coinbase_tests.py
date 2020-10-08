
import unittest

from selenium import webdriver

import config
import secure.creds
from pages.coinbase.homepage import HomePage
from pages.coinbase.signin import SigninPage


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



if __name__ == '__main__': unittest.main()
