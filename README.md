# ThePlatfrom
A python automation platform using selenium and unittest

## Support

Windows and Mac. Linux not supported.

## Setup

### Chromedriver

Chromedriver is untracked because people might have different versions of chrome. Get the version of Chromedriver that is appropriate for your browser and put it in /resources

### Add untracked files

The contents of /secure are untracked. You will need two files, creds.py and cookies.py. creds contains username/password combinations, cookies contains cookies.

Build creds.py
* `touch secure/creds.py`
* inside creds.py, declare `CBuser` with a string containing your username
* declare `CBpass` with a string containing your password

Build cookies.py
* Log in using selenium, choosing the option to skip two-factor auth next
               time
* Manually execute the two-factor auth
* Log out
* Do driver.get_cookies, print the results (it's a list), then copy to your clipboard
* In the terminal, `touch secure/cookies.py`
* Declare `cookies` and paste the driver.get_cookies results in as a string
** You may have to delete newlines in the middle of the dictionary keys/values

## How to use

In the root director of the repo (ThePlatform/), run `python coinbase_tests.py` to run all tests.  
Run `python coinbase_tests.py CLASS` to run all tests in a test case.  
Run `python coinbase_tests.py CLASS.TESTMETHOD` to run a specific test.  
