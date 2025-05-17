''' 
This module contains DDGo Search Page, the page object for the ddgo seatch page
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT= (By.ID, 'searchbox_input')
    
    def __init__(self, browser):
        self.browser=browser
    
    def load(self):
        self.browser.get(self.URL)
        
    def search(self, phrase):
        time.sleep(2)
        searchInput = self.browser.find_element(*self.SEARCH_INPUT)
        print('found the search box')
        searchInput.send_keys(phrase+Keys.RETURN)
        time.sleep(2)
        
        print('searching for panda')
