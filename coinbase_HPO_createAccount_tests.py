
from selenium import webdriver
import unittest
import platform
import os
import config
from pages.coinbase.homepage import HomePage
import tools.helpers

root_path = os.path.dirname(os.path.realpath(__file__))
if 'Darwin' in platform.system():
    chromedriver_path = config.mac_chromedriver_path
else: 
    chromedriver_path = config.win_chromedriver_path


class HomePageSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(root_path + config.win_chromedriver_path)
        self.page = HomePage(self.driver)
    
    def tearDown(self):

        self.page.driver.quit()


class HomePageCreateAccount(HomePageSetup):
    """
    Confirm that both create account buttons navigates to correct URL or 
    dialogue box.

    Acceptance Criteria
    -------------------
    -Clicking on the Get started button in the header navigates the user to the
     Create your account web page.
    -Clicking on the Get started button in the center of the page opens the
     Create account dialogue box.
    """

    def testGetStartedButtonHeader(self):

        page = self.page

        page.header_get_started_button.click()

        self.assertEqual(page.driver.title,
            'Coinbase – Buy & Sell Bitcoin, Ethereum, and more with trust')
        self.assertEqual(page.driver.current_url,
            'https://www.coinbase.com/signup')
    
    def testGetStartedButton(self):

        page = self.page

        page.get_started_button.click()

        self.assertTrue(page.account_dial_box.exists(),
        'create account is not opened when the Get started button is clicked')

if __name__ == '__main__': unittest.main()
