from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get('https://ezgif.com/webp-to-jpg')
browser.set_page_load_timeout(10)

browser.find_element(By.ID, "new-image").send_keys(r"C:\Users\Levon Grigoryan\Documents\QA15\selen2\Screenshots\home_page.png")

#browser.quit()