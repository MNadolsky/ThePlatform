
import config
from pages.templates.elements import *



class HomePage:

    def __init__(self, driver):

        driver.get(config.coinbase_domain)
        self.driver = driver

        self.build_elements()

    # NAVIGATION BAR

    home_link_loc =         (by.XPATH, "//a[@title='Home']")
    prices_link_loc =       (by.XPATH, "//a[@title='Prices']")
    products_menu_loc =     (by.XPATH, "//button[contains(text(),'Products')]")
    company_menu_loc =      (by.XPATH, "//button[contains(text(),'Company')]")
    earn_crypto_link_loc =  (by.XPATH, "//a[@title='Earn crypto']")
    sign_in_link_loc =      (by.XPATH, "//a[@title='Sign in']")
    header_get_started_button_loc =(by.XPATH, "//a[.='Get started']")

         
    # CREATE ACCOUNT

    get_started_email_field_loc =   (by.XPATH, "//input[@type='email']")
    get_started_button_loc =        (by.XPATH, "//input[@type='email']/following-sibling::button")

    # CRYPTO CURRENCY MENU

    bitcoin_text_link_loc =         (by.XPATH, "//h4[.='Bitcoin']")
    bitcoin_BTC_link_loc =          (by.XPATH, "//h4[.='BTC']")
    bitcoin_logo_link_loc =         (by.XPATH, "//img[@alt='Bitcoin logo']")
    bitcoin_price_button_loc =      (by.XPATH, "//a[@href='/price/bitcoin']/button")

    ethereum_text_link_loc =        (by.XPATH, "//h4[.='Ethereum']")
    ethereum_ETH_link_loc =         (by.XPATH, "//h4[.='ETH']") 
    ethereum_logo_link_loc =        (by.XPATH, "//img[@alt='Ethereum logo']")
    ethereum_price_button_loc =     (by.XPATH, "//a[@href='/price/ethereum']/button")

    bitcoinCash_text_link_loc =     (by.XPATH, "//h4[.='Bitcoin Cash']")        
    bitcoinCash_BCH_link_loc =      (by.XPATH, "//h4[.='BCH']")
    bitcoinCash_logo_link_loc =     (by.XPATH, "//img[@alt='Bitcoin Cash logo']")
    bitcoinCash_price_button_loc =  (by.XPATH, "//a[@href='/price/bitcoin-cash']/button")

    litecoin_text_link_loc =        (by.XPATH, "//h4[.='Litecoin']")
    litecoin_LTC_link_loc =         (by.XPATH, "//h4[.='LTC']")
    litecoin_logo_link_loc =        (by.XPATH, "//img[@alt='Litecoin logo']")
    litecoin_price_button_loc =     (by.XPATH, "//a[@href='/price/litecoin']/button")

    # EARNING LINKS BLCOK

    start_earning_button_loc =       (by.XPATH, "//button[contains(@class,'EarnUpsellBanner')]")
    start_earning_lower_button_loc = (by.XPATH, "//button[contains(@class,'EarnFooterBanner')]")
    maker_link_loc =                 (by.XPATH, "//a[@href='/earn/maker']/div")
    celo_link_loc =                  (by.XPATH, "//a[@href='/earn/celo']/div/div/h2")   #I don't love this xpath, but I feel it is the best way to locate this element
    compound_link_loc =              (by.XPATH, "//a[@href='/earn/compound']/div/div/h2")   #ditto
    EOS_link_loc =                   (by.XPATH, "//a[@href='/earn/eos']/div/div/h2")
    view_more_link_loc =             (by.XPATH, "//a[@href='/earn']/div")

    # MOBIL APPS
    
    android_app_link_loc =          (by.XPATH, "//a[contains(@href,'android')]")#='Android']")
    #ios_app_link_loc =              (by.XPATH, "//a[.='iOS']")

    # COINBASE SECURITY/INSURANCE
    '''
    security_link_loc =
    insurance_link_loc =
    best_practices_link_loc =

    # LANGUAGE MENU FOOTER

    language_menu_loc = 

    # PRODUCTS FOOTER

    coinbase_link_loc =
    commerce_link_loc =
    custody_link_loc =
    earn_link_loc =
    pro_link_loc =
    usd_coin_link_loc =
    
    # LEARN FOOTER

    browse_assets_link_loc =
    crypto_info_link_loc =
    bitcoin_info_link_loc =
    blockchain_info_link_loc =
    bitcoin_buy_link_loc =
    bitcoinCash_buy_link_loc =
    ethereum_buy_link_loc =
    litecoin_buy_link_loc =
    XRP_buy_link_loc =
    supported_countries_link_loc =
    status_link_loc =
    taxes_link_loc =

    # COMPANY FOOTER

    about_link_loc =
    affiliates_link_loc =
    careers_link_loc =
    partners_link_loc =
    press_link_loc =
    legal_and_privacy_link_loc =
    cookie_policy_link_loc =
    support_link_loc =

    # SOCIAL FOOTER

    blog_link_loc =
    twitter_link_loc =
    facebook_link_loc = '''


    def build_elements(self):

        # NAVIGATION BAR

        self.home_link =        Link(self.driver, self.home_link_loc)
        self.prices_link =      Link(self.driver, self.prices_link_loc)
        self.products_menu =    ReactiveMenu(self.driver,self.products_menu_loc)
        self.company_menu =     ReactiveMenu(self.driver, self.company_menu_loc)
        self.earn_crypto_link = Link(self.driver, self.earn_crypto_link_loc)
        self.sign_in_link =     Link(self.driver, self.sign_in_link_loc)
        self.header_get_started_button = Button(self.driver, self.header_get_started_button_loc)

        # CREATE ACCOUNT

        self.get_started_email_field =   Field(self.driver,self.get_started_email_field_loc)
        self.get_started_button =    Button(self.driver,self.get_started_button_loc)

        # CRYPTO CURRENCY MENU
  
        self.bitcoin_text_link =            Link(self.driver,self.bitcoin_text_link_loc)
        self.bitcoin_BTC_link =             Link(self.driver,self.bitcoin_BTC_link_loc)
        self.bitcoin_logo_link =            Link(self.driver,self.bitcoin_logo_link_loc)
        self.bitcoin_price_button =         Button(self.driver,self.bitcoin_price_button_loc)

        self.ethereum_text_link =           Link(self.driver,self.ethereum_text_link_loc)
        self.ethereum_ETH_link =            Link(self.driver,self.ethereum_ETH_link_loc)
        self.ethereum_logo_link =           Link(self.driver,self.ethereum_logo_link_loc)
        self.ethereum_price_button =        Button(self.driver,self.ethereum_price_button_loc)

        self.bitcoinCash_text_link =        Link(self.driver,self.bitcoinCash_text_link_loc)
        self.bitcoinCash_BCH_link =         Link(self.driver,self.bitcoinCash_BCH_link_loc)
        self.bitcoinCash_logo_link =        Link(self.driver,self.bitcoinCash_logo_link_loc)
        self.bitcoinCash_price_button =     Button(self.driver,self.bitcoinCash_price_button_loc)
        
        self.litecoin_text_link =           Link(self.driver,self.litecoin_text_link_loc)
        self.litecoin_LTC_link =            Link(self.driver,self.litecoin_LTC_link_loc)
        self.litecoin_logo_link =           Link(self.driver,self.litecoin_logo_link_loc)
        self.litecoin_price_button =        Button(self.driver,self.litecoin_price_button_loc)

        # EARNING LINKS BLCOK

        self.start_earning_button =             Button(self.driver,self.start_earning_button_loc)
        self.start_earning_lower_button =       Button(self.driver,self.start_earning_lower_button_loc)
        self.maker_link =                       Link(self.driver,self.maker_link_loc)
        self.celo_link =                        Link(self.driver,self.celo_link_loc)
        self.compound_link =                    Link(self.driver,self.compound_link_loc)
        self.EOS_link =                         Link(self.driver,self.EOS_link_loc)
        self.view_more_link =                   Link(self.driver,self.view_more_link_loc)

        # MOBIL APPS

        self.android_app_link =         Link(self.driver,self.android_app_link_loc)
        #self.ios_app_link =             Link(self.driver,self.ios_app_link_loc)
        '''
        # COINBASE SECURITY/INSURANCE

        self.ios_app_link =             Link(self.driver,self.ios_app_link_loc)
        self.insurance_link =           Link(self.driver,self.insurance_link_loc)
        self.best_practices_link =      Link(self.driver,self.best_practices_link_loc)

        # LANGUAGE MENU FOOTER

        self.language_menu =            ReactiveMenu(self.driver,self.language_menu_loc)

        # PRODUCTS FOOTER

        self.coinbase_link =            Link(self.driver,self.coinbase_link_loc)
        self.commerce_link =            Link(self.driver,self.commerce_link_loc)
        self.custody_link =             Link(self.driver,self.custody_link_loc)
        self.earn_link =                Link(self.driver,self.earn_link_loc)
        self.pro_link =                 Link(self.driver,self.pro_link_loc)
        self.usd_coin_link =            Link(self.driver,self.usd_coin_link_loc)
        
        # LEARN FOOTER

        self.browse_assets_link =       Link(self.driver,self.browse_assets_link_loc)
        self.crypto_info_link =         Link(self.driver,self.crypto_info_link_loc)
        self.bitcoin_info_link =        Link(self.driver,self.bitcoin_info_link_loc)
        self.blockchain_info_link =     Link(self.driver,self.blockchain_info_link_loc)
        self.bitcoin_buy_link =         Link(self.driver,self.bitcoin_buy_link_loc)
        self.bitcoinCash_buy_link =     Link(self.driver,self.bitcoinCash_buy_link_loc)
        self.ethereum_buy_link =        Link(self.driver,self.ethereum_buy_link_loc)
        self.litecoin_buy_link =        Link(self.driver,self.litecoin_buy_link_loc)
        self.XRP_buy_link =             Link(self.driver,self.XRP_buy_link_loc)
        self.supported_countries_link = Link(self.driver,self.supported_countries_link_loc)
        self.status_link =              Link(self.driver,self.status_link_loc)   
        self.taxes_link =               Link(self.driver,self.taxes_link_loc)

        # COMPANY FOOTER

        self.about_link =               Link(self.driver,self.about_link_loc)
        self.affiliates_link =          Link(self.driver,self.affiliates_link_loc)
        self.careers_link =             Link(self.driver,self.careers_link_loc)
        self.partners_link =            Link(self.driver,self.partners_link_loc)
        self.press_link =               Link(self.driver,self.press_link_loc)
        self.legal_and_privacy_link =   Link(self.driver,self.legal_and_privacy_link_loc)
        self.cookie_policy_link =       Link(self.driver,self.cookie_policy_link_loc)
        self.support_link =             Link(self.driver,self.support_link_loc)

        # SOCIAL FOOTER

        self.blog_link =                Link(self.driver,self.blog_link_loc)
        self.twitter_link =             Link(self.driver,self.twitter_link_loc)
        self.facebook_link =            Link(self.driver,self.facebook_link_loc)'''