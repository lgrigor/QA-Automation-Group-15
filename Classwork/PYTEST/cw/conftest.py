import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setUp(request):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    yield browser

    tc = request.node.name
    browser.save_screenshot(str(tc) + '.png')
    browser.quit()
