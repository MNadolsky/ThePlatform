
import unittest
import time

from selenium import webdriver

import config
import secure.creds
from pages.coinbase.homepage import HomePage
from pages.coinbase.signin import SigninPage
from pages.coinbase.dashboard import DashboardPage



class Login(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(config.chromedriver_path)
        self.page = SigninPage(driver, spawn=True)

    def runTest(self):
        """
        Confirm that logging in succeeds.

        Acceptance Criteria
        --------------------
        - When a valid username and password combination is submitted through
          /signin the user is directed to /dashboard and signed in
        """

        page = self.page

        page.email_field.input(secure.creds.CBuser)
        page.pass_field.input(secure.creds.CBpass)
        page.sign_in_button.click()

        self.assertEqual \
            (page.driver.current_url, config.coinbase_domain + '/dashboard')
        self.assertEqual \
            (page.driver.title, 'Coinbase')

        self.assertTrue('user is', 'logged in')

    def tearDown(self):

        self.page.driver.quit()




class LoginErrors(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(config.chromedriver_path)
        self.page = SigninPage(driver, spawn=True, bypass_auth=False)

    def testWrongUsername(self):

        page = self.page

        page.email_field.input('a' + secure.creds.CBuser)
        page.pass_field.input(secure.creds.CBpass)
        page.sign_in_button.click()

        self.assertTrue(page.sign_in_error_alert.exists())
        self.assertEqual(
            page.sign_in_error_alert.element().get_attribute('style'), '')

    def testWrongPassword(self):

        page = self.page

        page.email_field.input(secure.creds.CBuser)
        page.pass_field.input('a' + secure.creds.CBpass)
        page.sign_in_button.click()

        self.assertTrue(page.sign_in_error_alert.exists())
        self.assertEqual(
            page.sign_in_error_alert.element().get_attribute('style'), '')

    def testNoUsername(self):

        page = self.page

        page.pass_field.input(secure.creds.CBpass)
        page.sign_in_button.click()

        self.assertTrue(page.sign_in_error_alert.exists())
        self.assertEqual(
            page.sign_in_error_alert.element().get_attribute('style'), '')

    def testNoPassword(self):

        page = self.page

        page.email_field.input(secure.creds.CBuser)
        page.sign_in_button.click()

        self.assertTrue(page.sign_in_error_alert.exists())
        self.assertEqual(
            page.sign_in_error_alert.element().get_attribute('style'), '')

    def tearDown(self):

        self.page.driver.quit()




class Logout(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(config.chromedriver_path)
        page = SigninPage(driver, spawn=True)
        page.login()
        self.page = DashboardPage(driver)

    def runTest(self):
        """
        Confirm that loggin out succeeds

        Acceptance Criteria
        - When a user logs out via the avatar menu he is redirected to
          /signin and cannot reach /dashboard without loggin in again
        """

        page = self.page

        page.avatar_menu.select('Sign out')

        self.assertEqual \
            (page.driver.title, 'Coinbase - Buy/Sell Digital Currency')
        self.assertEqual \
            (page.driver.current_url, config.coinbase_domain + '/signin')

        self.assertTrue('user cannot', 'reach dashboard')

    def tearDown(self):

        self.page.driver.quit()







if __name__ == '__main__': unittest.main()
