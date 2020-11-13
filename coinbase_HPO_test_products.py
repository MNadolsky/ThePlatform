
from selenium import webdriver
import unittest
import platform
import os
import config
import secure.creds
from pages.coinbase.homepage import HomePage
from tools.helpers import Tools

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
    -All of the provided featured products are listed in any order.
    -All of the provided featured products are listed in order.
    -When clicking on any of these products link it opens the "create new
     account dialogue box".   
    """

    def testProductsExistAnyOrder(self):

        provided_featured_product_list = ['Bitcoin\nBTC', 'Ethereum\nETH',
                                          'Bitcoin Cash\nBCH', 'Litecoin\nLTC']  

        featured_product_list_text = Tools().format_element_list_to_text_list(
            self.page.featured_product_list)
        
        self.assertTrue(Tools().compare_two_lists_sequence_ind(
            featured_product_list_text, provided_featured_product_list), 
            'A product from the provided featured list has been removed or'
            + ' changed')

    def testProductsExistInOrder(self):

        provided_featured_product_acronym_list = ['BTC', 'ETH','BCH', 'LTC']

        provided_featured_product_name_list = ['Bitcoin', 'Ethereum',
                                               'Bitcoin Cash', 'Litecoin']

        page = self.page

        self.assertEqual(provided_featured_product_acronym_list[0],
            self.driver.find_element(*page.bitcoin_BTC_link_loc).text)
        self.assertEqual(provided_featured_product_acronym_list[1],
            self.driver.find_element(*page.ethereum_ETH_link_loc).text)
        self.assertEqual(provided_featured_product_acronym_list[2],
            self.driver.find_element(*page.bitcoinCash_BCH_link_loc).text)
        self.assertEqual(provided_featured_product_acronym_list[3],
            self.driver.find_element(*page.litecoin_LTC_link_loc).text)

        self.assertEqual(provided_featured_product_name_list[0],
            self.driver.find_element(*page.bitcoin_text_link_loc).text)
        self.assertEqual(provided_featured_product_name_list[1],
            self.driver.find_element(*page.ethereum_text_link_loc).text)
        self.assertEqual(provided_featured_product_name_list[2],
            self.driver.find_element(*page.bitcoinCash_text_link_loc).text)
        self.assertEqual(provided_featured_product_name_list[3],
            self.driver.find_element(*page.litecoin_text_link_loc).text)

    def testProductsLink(self):

        self.page.total_product_link_list[
            Tools().generate_random_num(1,16)].click()
        self.assertTrue(self.page.create_account_dial_box.exists(),
        'create account is not opened when bitcoin text is clicked')


if __name__ == '__main__': unittest.main()
