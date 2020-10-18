
"""
This modules is for facilitating page objects methods to return different page
objects by abstracting all the function in a single location (this eliminates 
the need, for example, every page object to import every other page object) and 
mitigating the consequences of the necessary circular imports.

How to use:

Call the get_page function with a driver (driver) and a string (destingation) 
representing the page object you want to get. The destination string needs to
correspond to the approprate _function. If you want to get a HomePage object,
destination = 'home' (for the _function _home()), if you want to get a 
SigninPage object, destination = 'signin' (for the _function _signin()), etc.

So if you do page = get_page(driver, 'dashboard'), page would be a DashboardPage
object.

Note: This is meant to enable .click() functions that direct to a new page to be
able to retun the page object of the new page. Therefore, there is no option to
use the spawn page object parameter.
"""

def get_page(driver, destination):

    foo = globals().copy()
    foo.update(locals())
    func = foo.get('_' + destination)
    return func(driver)

def _home(driver):
    from pages.coinbase.homepage import HomePage
    return HomePage(driver)

def _signin(driver):
    from pages.coinbase.signin import SigninPage
    return SigninPage(driver)

def _dashboard(driver):
    from pages.coinbase.dashboard import DashboardPage
    return DashboardPage(driver)
