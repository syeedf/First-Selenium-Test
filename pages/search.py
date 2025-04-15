''' 
This module contains DDGo Search Page, the page object for the ddgo seatch page
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    url= 'https://www.duckduckgo.com'
    search_input= (By.id, 'searchbox_input')
    
    def __init__(self, browser):
        self.browser=browser
    
    def load(self):
        self.browser.get(self.url)
        
    def search(self, phrase):
        #TODO
        pass
