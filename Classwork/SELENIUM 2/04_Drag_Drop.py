from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://jqueryui.com/droppable/")

browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

source = browser.find_element(By.ID, 'draggable')
target = browser.find_element(By.ID, 'droppable')

#time.sleep(1)
action_chains = ActionChains(browser)
action_chains.drag_and_drop(source, target).perform()
