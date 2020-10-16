
def get_page(driver, destination):

    foo = globals().copy()
    foo.update(locals())
    func = foo.get(destination)
    return func(driver)

def home(driver):
    from pages.coinbase.homepage import HomePage
    return HomePage(driver)

def signin(driver):
    from pages.coinbase.signin import SigninPage
    return SigninPage(driver)

def dashboard(driver):
    from pages.coinbase.dashboard import DashboardPage
    return DashboardPage(driver)
