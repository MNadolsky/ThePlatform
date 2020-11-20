
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


class HomePageSignIn(HomePageSetup):
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
