
import unittest
import time
import os

from selenium import webdriver

import config
import secure.creds
from pages.coinbase.homepage import HomePage



class HomePageSetup(unittest.TestCase):

    def setUp(self):
        root_path = os.path.dirname(os.path.realpath(__file__))
        driver = webdriver.Chrome(root_path + config.win_chromedriver_path)
        self.page = HomePage(driver)
    
    def tearDown(self):

        self.page.driver.quit()

class HomePageProducts(HomePageSetup):
    """
    Confirm the list of featured products are present on homepage. Ensure that
    clicking on each product link will navigate to the create a new account
    dialogue box.

    acceptance cirteria
    --------------------
    -All of the provided feature products are listed in any order.
    -When clicking on any of these product links the create new account 
    dialogue box appears.   
    """
    
    def testProductsExist(self):

        page = self.page
