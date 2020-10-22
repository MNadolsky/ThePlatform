
import config
from pages.templates.elements import *
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver, close_cookie_banner=True):

        driver.get(config.coinbase_domain)

        self.build_elements()

        if close_cookie_banner:
            wait(driver,10).until(EC.visibility_of_element_located(
                self.visible_cookie_banner_loc))
            self.cookie_banner_dismiss_button.click()
    
        self.driver = driver    #this needs to be before the button to be able to load the button duhhh


    # A dismiss cookie dialogue box appears and hides elements, clicking
    # the dismiss button performed in the init method fixes this issue  
    visible_cookie_banner_loc = (by.XPATH, "//div[@class='sc-fzoLsD gkNzOD']")
    cookie_banner_dismiss_button_loc = (by.XPATH, "//button[.='Dismiss']")

    # NAVIGATION BAR

    home_link_loc =         (by.XPATH, "//a[@title='Home']")
    prices_link_loc =       (by.XPATH, "//a[@title='Prices']")
    products_menu_loc =     (by.XPATH, "//button[contains(text(),'Products')]")
    company_menu_loc =      (by.XPATH, "//button[contains(text(),'Company')]")
    earn_crypto_link_loc =  (by.XPATH, "//a[@title='Earn crypto']")
    sign_in_link_loc =      (by.XPATH, "//a[@title='Sign in']")
    header_get_started_button_loc = (by.XPATH, "//a[.='Get started']")

         
    # CREATE ACCOUNT

    email_address_field_loc = (by.XPATH, "//input[@type='email']")
    get_started_button_loc =  (by.XPATH,
                            "//input[@type='email']/following-sibling::button")

    # CRYPTO CURRENCY MENU

    bitcoin_text_link_loc =    (by.XPATH, "//h4[.='Bitcoin']")
    bitcoin_BTC_link_loc =     (by.XPATH, "//h4[.='BTC']")
    bitcoin_logo_link_loc =    (by.XPATH, "//img[@alt='Bitcoin logo']")
    bitcoin_buy_button_loc =   (by.XPATH, "//a[@href='/price/bitcoin']/button")

    ethereum_text_link_loc =  (by.XPATH, "//h4[.='Ethereum']")
    ethereum_ETH_link_loc =   (by.XPATH, "//h4[.='ETH']") 
    ethereum_logo_link_loc =  (by.XPATH, "//img[@alt='Ethereum logo']")
    ethereum_buy_button_loc=  (by.XPATH, "//a[@href='/price/ethereum']/button")

    bitcoinCash_text_link_loc =   (by.XPATH, "//h4[.='Bitcoin Cash']")        
    bitcoinCash_BCH_link_loc =    (by.XPATH, "//h4[.='BCH']")
    bitcoinCash_logo_link_loc =   (by.XPATH, "//img[@alt='Bitcoin Cash logo']")
    bitcoinCash_buy_button_loc =  (by.XPATH,
                                   "//a[@href='/price/bitcoin-cash']/button")

    litecoin_text_link_loc =  (by.XPATH, "//h4[.='Litecoin']")
    litecoin_LTC_link_loc =   (by.XPATH, "//h4[.='LTC']")
    litecoin_logo_link_loc =  (by.XPATH, "//img[@alt='Litecoin logo']")
    litecoin_buy_button_loc=  (by.XPATH, "//a[@href='/price/litecoin']/button")

    # EARNING LINKS BLCOK

    start_earning_button_loc = (by.XPATH,
                               "//button[contains(@class,'EarnUpsellBanner')]")
    footer_start_earning_button_loc = (by.XPATH,
                               "//button[contains(@class,'EarnFooterBanner')]")
    maker_link_loc =          (by.XPATH, "//a[@to='/earn/maker']")
    celo_link_loc =           (by.XPATH, "//a[@to='/earn/celo']")  
    compound_link_loc =       (by.XPATH, "//a[@to='/earn/compound']") 
    EOS_link_loc =            (by.XPATH, "//a[@to='/earn/eos']")
    view_more_link_loc =      (by.XPATH, "//a[@to='/earn']")

    # MOBILE APPS
    
    android_app_link_loc =        (by.XPATH, "//a[contains(@href,'android')]")
    ios_app_link_loc =            (by.XPATH, "//a[.='iOS']")

    # COINBASE SECURITY/INSURANCE

    secure_storage_link_loc =       (by.XPATH,
        "//a[@title='Learn how Coinbase keeps your funds safe and secure']")     
    protected_insurance_link_loc =      (by.XPATH,
        "//a[@title=" +
        "'Learn how your crypto is covered by our insurance policy']")  #I see how to PEP 8 format for a long string but doing this breaks the XPATH, so these two lines went over the 79 characters   
    industry_best_practices_link_loc = (by.XPATH,
        "//a[@title='Learn how we implement industry best practices for account security']")

    # LANGUAGE MENU FOOTER

    language_menu_loc =      (by.XPATH,"//select[contains(@class,'Language')]")

    # PRODUCTS FOOTER

    coinbase_link_loc =             (by.XPATH, "//a[.='Coinbase']")   
    commerce_link_loc =             (by.XPATH, "//a[.='Commerce']")
    custody_link_loc =              (by.XPATH, "//a[.='Custody']")
    earn_link_loc =                 (by.XPATH, "//a[.='Earn']")
    pro_link_loc =                  (by.XPATH, "//a[.='Pro']")
    usd_coin_link_loc =             (by.XPATH, "//a[.='USD Coin']")
    wallet_link_loc =               (by.XPATH, "//a[.='Wallet']")
    ventures_link_loc =             (by.XPATH, "//a[.='Ventures']")
    
    # LEARN FOOTER

    browse_assets_link_loc =        (by.XPATH, "//a[.='Browse assets']")
    what_is_crypto_link_loc =       (by.XPATH, "//a[.='What is Crypto?']")
    what_is_bitcoin_link_loc =      (by.XPATH, "//a[.='What is Bitcoin?']")
    what_is_blockchain_link_loc =   (by.XPATH, "//a[.='What is Blockchain?']")
    buy_bitcoin_link_loc =          (by.XPATH, "//a[.='Buy Bitcoin']")
    buy_bitcoinCash_link_loc =      (by.XPATH, "//a[.='Buy Bitcoin Cash']")
    buy_ethereum_link_loc =         (by.XPATH, "//a[.='Buy Ethereum']")
    buy_litecoin_link_loc =         (by.XPATH, "//a[.='Buy Litecoin']")
    buy_XRP_link_loc =              (by.XPATH, "//a[.='Buy XRP']")
    supported_countries_link_loc =  (by.XPATH, "//a[.='Supported countries']")
    status_link_loc =               (by.XPATH, "//a[.='Status']")
    taxes_link_loc =                (by.XPATH, "//a[.='Taxes']")

    # COMPANY FOOTER

    about_link_loc =                (by.XPATH, "//a[.='About']")
    affiliates_link_loc =           (by.XPATH, "//a[.='Affiliates']")
    careers_link_loc =              (by.XPATH, "//a[.='Careers']")
    partners_link_loc =             (by.XPATH, "//a[.='Partners']")
    press_link_loc =                (by.XPATH, "//a[.='Press']")
    legal_and_privacy_link_loc =    (by.XPATH, "//a[.='Legal & Privacy']")
    cookie_policy_link_loc =        (by.XPATH, "//a[.='Cookie Policy']")
    support_link_loc =              (by.XPATH, "//a[.='Support']")

    # SOCIAL FOOTER

    blog_link_loc =                 (by.XPATH, "//a[.='Blog']")
    twitter_link_loc =              (by.XPATH, "//a[.='Twitter']")
    facebook_link_loc =             (by.XPATH, "//a[.='Facebook']")


    def build_elements(self):

        # COOKIE BANNER

        self.cookie_banner_dismiss_button =  Button(self.driver,self.cookie_banner_dismiss_button_loc)

        # NAVIGATION BAR

        self.home_link =       Link(self.driver, self.home_link_loc)
        self.prices_link =     Link(self.driver, self.prices_link_loc)
        self.products_menu =   ReactiveMenu(self.driver,self.products_menu_loc)
        self.company_menu =    ReactiveMenu(self.driver, self.company_menu_loc)
        self.earn_crypto_link= Link(self.driver, self.earn_crypto_link_loc)
        self.sign_in_link =    Link(self.driver, self.sign_in_link_loc)
        self.header_get_started_button = Button(self.driver,
                                            self.header_get_started_button_loc)

        # CREATE ACCOUNT

        self.email_address_field = Field(self.driver,
                                         self.email_address_field_loc)
        self.get_started_button =  Button(self.driver,
                                          self.get_started_button_loc)

        # CRYPTO CURRENCY MENU
  
        self.bitcoin_text_link =  Link(self.driver,self.bitcoin_text_link_loc)
        self.bitcoin_BTC_link =   Link(self.driver,self.bitcoin_BTC_link_loc)
        self.bitcoin_logo_link =  Link(self.driver,self.bitcoin_logo_link_loc)
        self.bitcoin_buy_button = Button(
                                       self.driver,self.bitcoin_buy_button_loc)

        self.ethereum_text_link = Link(self.driver,self.ethereum_text_link_loc)
        self.ethereum_ETH_link =  Link(self.driver,self.ethereum_ETH_link_loc)
        self.ethereum_logo_link = Link(self.driver,self.ethereum_logo_link_loc)
        self.ethereum_buy_button = Button(self.driver,
                                            self.ethereum_buy_button_loc)

        self.bitcoinCash_text_link =  Link(self.driver,
                                            self.bitcoinCash_text_link_loc)
        self.bitcoinCash_BCH_link =   Link(self.driver,
                                            self.bitcoinCash_BCH_link_loc)
        self.bitcoinCash_logo_link =  Link(self.driver,
                                            self.bitcoinCash_logo_link_loc)
        self.bitcoinCash_buy_button = Button(self.driver,
                                            self.bitcoinCash_buy_button_loc)
        
        self.litecoin_text_link = Link(self.driver,self.litecoin_text_link_loc)
        self.litecoin_LTC_link =  Link(self.driver,self.litecoin_LTC_link_loc)
        self.litecoin_logo_link = Link(self.driver,self.litecoin_logo_link_loc)
        self.litecoin_buy_button = Button(self.driver,
                                            self.litecoin_buy_button_loc)

        # EARNING LINKS BLCOK

        self.start_earning_button = Button(self.driver,
                                          self.start_earning_button_loc)
        self.footer_start_earning_button = Button(self.driver,
                                          self.footer_start_earning_button_loc)
        self.maker_link =     Link(self.driver,self.maker_link_loc)
        self.celo_link =      Link(self.driver,self.celo_link_loc)
        self.compound_link =  Link(self.driver,self.compound_link_loc)
        self.EOS_link =       Link(self.driver,self.EOS_link_loc)
        self.view_more_link = Link(self.driver,self.view_more_link_loc)

        # MOBIL APPS

        self.android_app_link = Link(self.driver,self.android_app_link_loc)
        self.ios_app_link =     Link(self.driver,self.ios_app_link_loc)

        # COINBASE SECURITY/INSURANCE

        self.secure_storage_link =          Link(self.driver,
                                         self.secure_storage_link_loc)
        self.protected_insurance_link =     Link(self.driver,
                                         self.protected_insurance_link_loc)
        self.industry_best_practices_link = Link(self.driver,
                                         self.industry_best_practices_link_loc)

        # LANGUAGE MENU FOOTER

        self.language_menu = ReactiveMenu(self.driver,self.language_menu_loc)

        # PRODUCTS FOOTER

        self.coinbase_link = Link(self.driver,self.coinbase_link_loc)
        self.commerce_link = Link(self.driver,self.commerce_link_loc)
        self.custody_link =  Link(self.driver,self.custody_link_loc)
        self.earn_link =     Link(self.driver,self.earn_link_loc)
        self.pro_link =      Link(self.driver,self.pro_link_loc)
        self.usd_coin_link = Link(self.driver,self.usd_coin_link_loc)
        self.wallet_link =   Link(self.driver,self.wallet_link_loc)
        self.ventures_link = Link(self.driver,self.ventures_link_loc)

        # LEARN FOOTER

        self.browse_assets_link = Link(self.driver,self.browse_assets_link_loc)
        self.what_is_crypto_link =     Link(self.driver,
                                            self.what_is_crypto_link_loc)
        self.what_is_bitcoin_link =    Link(self.driver,
                                            self.what_is_bitcoin_link_loc)
        self.what_is_blockchain_link = Link(self.driver,
                                            self.what_is_blockchain_link_loc)
        self.buy_bitcoin_link =    Link(self.driver,self.buy_bitcoin_link_loc)
        self.buy_bitcoinCash_link= Link(self.driver,
                                         self.buy_bitcoinCash_link_loc)
        self.buy_ethereum_link =   Link(self.driver,self.buy_ethereum_link_loc)
        self.buy_litecoin_link =   Link(self.driver,self.buy_litecoin_link_loc)
        self.buy_XRP_link =        Link(self.driver,self.buy_XRP_link_loc)
        self.supported_countries_link = Link(self.driver,
                                             self.supported_countries_link_loc)
        self.status_link =         Link(self.driver,self.status_link_loc)   
        self.taxes_link =          Link(self.driver,self.taxes_link_loc)

        # COMPANY FOOTER

        self.about_link =         Link(self.driver,self.about_link_loc)
        self.affiliates_link =    Link(self.driver,self.affiliates_link_loc)
        self.careers_link =       Link(self.driver,self.careers_link_loc)
        self.partners_link =      Link(self.driver,self.partners_link_loc)
        self.press_link =         Link(self.driver,self.press_link_loc)
        self.legal_and_privacy_link =   Link(self.driver,
                                             self.legal_and_privacy_link_loc)
        self.cookie_policy_link = Link(self.driver,self.cookie_policy_link_loc)
        self.support_link =       Link(self.driver,self.support_link_loc)

        # SOCIAL FOOTER

        self.blog_link =          Link(self.driver,self.blog_link_loc)
        self.twitter_link =       Link(self.driver,self.twitter_link_loc)
        self.facebook_link =      Link(self.driver,self.facebook_link_loc)
