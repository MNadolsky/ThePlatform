
from selenium import webdriver
import unittest
import platform
import os
import config
import secure.creds
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


class HomePageProducts(HomePageSetup):
    """
    Confirm the list of the companie's featured products are present on
    homepage. Ensure that clicking on each product link will navigate to the
    dialogue box 'create a new account'.

    acceptance cirteria
    --------------------
    -All of the provided featured products are listed.
    -When clicking on a random product link it opens the "create new account
     dialogue box".   
    """

    def testProductsExist(self):
        #below is mock data set representing a source of truth 
        provided_featured_products = {'Bitcoin\nBTC', 'Ethereum\nETH', 
                                      'Bitcoin Cash\nBCH', 'Litecoin\nLTC'} 

        #featured products retrieved from coinbase
        featured_products = set() 
        for element in self.page.featured_product_list:
            featured_products.add(element.text)
        
        self.assertEqual(featured_products, provided_featured_products)

    def testProductsLink(self):
        page = self.page
        
        for product in page.products_links:
            product.click()
            self.assertTrue(page.account_dial_box.exists(),
            'create account is not opened when the ' + product.element().text +
            ' link is clicked')
            page.account_dial_box_close.click()


if __name__ == '__main__': unittest.main()
