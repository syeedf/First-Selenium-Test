''' This module contains DDGOResult page
'''
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage: 

    RESULT_LINKS = (By.CLASS_NAME,"EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk")
    SEARCH_INPUT= (By.ID, 'searchbox_input')

    #Initializer 

    def __init__(self, browser):
        self.browser = browser
    
    #returns a list of web page titles from the search on the result page 
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        webtitles= [link.text for link in links]
        return webtitles 
    
    
    def search_input_value(self):
        search_input= self.browser.find_element(*self.SEARCH_INPUT)
        value= search_input.get_attribute('value')
        return value 
    
    def title(self):
        return self.browser.title