"""
these test cover duckduckgo searches

"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):

    search_page=DuckDuckGoSearchPage(browser)
    result_page=DuckDuckGoResultPage(browser)
    phrase= "panda"
    
    #Given the duckduckgo home page is displayed
    search_page.load()
    #When the user searches for "panda"
    search_page.search(phrase)

    #Then the search result title contains "panda"
    assert phrase in result_page.title()

    #And the search result query is "panda"
    assert phrase== result_page.search_input_value()

    #And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

