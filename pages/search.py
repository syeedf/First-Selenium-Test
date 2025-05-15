''' 
This module contains DDGo Search Page, the page object for the ddgo seatch page
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT= (By.ID, 'searchbox_input')
    
    def __init__(self, browser):
        self.browser=browser
    
    def load(self):
        self.browser.get(self.URL)
        
    def search(self, phrase):
        searchInput = self.browser.find_element(*self.SEARCH_INPUT)
        searchInput.send_keys(phrase + Keys.RETURN)
        print('searching for panda')
