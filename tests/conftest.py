"""
SHared fixture file

"""
import json 
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    # read the file 
    with open('config.json') as config_file: 
        config= json.load(config_file)

    #assert values are acceptable 
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    
    # return the config 
    return config



@pytest.fixture
def browser(config):

    #initialize chromedriver
    if config['browser']== 'Chrome':
        b =selenium.webdriver.Chrome()
    elif config['browser']=='FireFox':
        b=selenium.webdriver.Firefox()
    elif config['browser']=='Headless Chrome':
        opts=selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b=selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser " {config["browser"]}" is not supported')
    #waits 10 sec for elements to appear
    b.implicitly_wait(config['implicit_wait'])
    # return the webdriver for setup
    yield b
    #quit webdriver instance
    b.quit()
    