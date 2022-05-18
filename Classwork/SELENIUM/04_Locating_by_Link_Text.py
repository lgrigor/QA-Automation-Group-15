from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

#chrome_options = Options()
#chrome_options.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(r'C:\Users\Levon Grigoryan\Desktop\here\chromedriver.exe'))
browser.get(r"C:\Users\Levon Grigoryan\Documents\QA15\selen\04_page_source.html")

#continue_link = browser.find_element(By.LINK_TEXT, 'Continue')
continue_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'tin')

continue_link.click()