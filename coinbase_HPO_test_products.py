
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
        #the source of truth is the provided_featured_product_set
        provided_featured_product_set = {'Bitcoin\nBTC', 'Ethereum\nETH', 
                                          'Bitcoin Cash\nBCH', 'Litecoin\nLTC'}  
        #the set of products from coinbase is the featured_product_set
        #featured_product_set = set() 
            #featured_product_set.add(element.text)

        for product in self.page.product_link_list:
            self.assertIn(product.element().text,provided_featured_product_set)

        #self.assertEqual(featured_product_set, provided_featured_product_set)

    def testProductsLink(self):
        page = self.page
        random_product_num = tools.helpers.generate_random_num(1,16)
        #a randomly chosen product is below
        page.product_link_list[random_product_num].click()

        self.assertTrue(page.account_dial_box.exists(),
        'create account is not opened when the number ' +
        str(random_product_num)+' link of the product link list is clicked')

        page.account_dial_box_close.click()

if __name__ == '__main__': unittest.main()
