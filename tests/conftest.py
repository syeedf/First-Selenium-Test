"""
SHared fixture file

"""

import pytest
import selenium.webdriver

@pytest.fixture

def browser():

    #initialize chromedriver
    b =selenium.webdriver.Chrome()

    #waits 10 sec for elements to appear
    b.implicitly_wait(10)
    # return the webdriver for setup
    yield b
    #quit webdriver instance
    b.quit()
    