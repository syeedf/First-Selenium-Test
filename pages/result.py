''' This module contains DDGOResult page
'''
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage: 

    RESULT_LINKS = (By.CSS_SELECTOR,"[data-testid='result-title-a']")
    SEARCH_INPUT= (By.ID, 'searchbox_input')
    def __init__(self, browser):
        self.browser = browser
    
    def result_link_titles(self):
        #TODO
        return[]
    
    def search_input_value(self):
        #TODO
        return ""
    
    def title(self):
        #TODO
        return ""