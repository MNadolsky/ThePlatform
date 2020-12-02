
import unittest
import platform
import os
import time

from selenium import webdriver

import config
import secure.creds
from pages.coinbase.homepage import HomePage
from pages.coinbase.signin import SigninPage
from pages.coinbase.dashboard import DashboardPage



root_path = os.path.dirname(os.path.realpath(__file__))
if 'Darwin' in platform.system():
    chromedriver_path = config.mac_chromedriver_path
else: 
    chromedriver_path = config.win_chromedriver_path

class Login(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(root_path + chromedriver_path)
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

        driver = webdriver.Chrome(root_path + chromedriver_path)
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

        driver = webdriver.Chrome(root_path + chromedriver_path)
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
            (page.driver.title, 'Coinbase - Buy/Sell Cryptocurrency')
        self.assertEqual \
            (page.driver.current_url, config.coinbase_domain + '/signin')

        self.assertTrue('user cannot', 'reach dashboard')

    def tearDown(self):

        self.page.driver.quit()

class HomePageSetupTemplate(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(root_path + config.win_chromedriver_path)
        self.page = HomePage(self.driver)
    
    def tearDown(self):

        self.page.driver.quit()


class HomePageSignIn(HomePageSetupTemplate):
    """
    Ensure clicking on the sign in link will navigate the user to the sign in 
    page.

    acceptance criteria
    ------------------- 
    -Clicking the sign in button navigates to the sign in url.
    """

    def testSignIn(self):

        page = self.page

        page.sign_in_link.click()

        self.assertEqual \
            (page.driver.title, 'Coinbase - Buy/Sell Cryptocurrency')
        self.assertEqual \
            (page.driver.current_url,'https://www.coinbase.com/signin')


if __name__ == '__main__': unittest.main()
