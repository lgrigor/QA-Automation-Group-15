from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://www.youtube.com/")

browser.find_element(By.XPATH, "//ytd-searchbox[@id='search']").send_keys('zartir lao mernim qiz')
browser.find_element(By.XPATH, "//ytd-searchbox[@id='search']").send_keys(Keys.ENTER)

time.sleep(3)
browser.refresh()

time.sleep(3)
browser.back()

time.sleep(3)
browser.forward()