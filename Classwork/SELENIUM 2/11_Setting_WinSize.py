from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
#chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--window-size=600,600')

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get(r'C:\Users\Levon Grigoryan\Documents\QA15\selen2\06_Page_Source.html')

time.sleep(3)
browser.set_window_size(1000, 1000)