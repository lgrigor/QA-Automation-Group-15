import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=3).install()), options=chrome_options)

    yield browser

    browser.quit()