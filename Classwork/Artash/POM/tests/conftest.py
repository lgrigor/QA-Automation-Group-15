from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def setup():

    #browser = webdriver.Chrome(Service = Service(ChromeDriverManager(log_level=3).install()))
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--capture=no")
    chrome_options.add_argument("--log-level=3")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield browser
    browser.quit()
