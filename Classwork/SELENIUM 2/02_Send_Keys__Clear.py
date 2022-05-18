from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

TEST_TEXT = 'abracadabr'
BASE_URL = "https://www.google.com/"

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get(BASE_URL)

form = browser.find_element(By.CSS_SELECTOR, "input[name='q']")
form.send_keys(TEST_TEXT)

time.sleep(2)

form.send_keys('a')
form.send_keys(Keys.LEFT_SHIFT, 'a')


# form.send_keys(TEST_TEXT)
# 