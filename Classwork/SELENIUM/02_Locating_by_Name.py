from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

#chrome_options = Options()
#chrome_options.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(r'C:\Users\Levon Grigoryan\Desktop\here\chromedriver'))
browser.get("https://www.facebook.com/")

#browser.find_element_by_name('email').send_keys('levon.grigoryan97@gmail.com')
browser.find_element(By.NAME, 'email').send_keys('levon.grigoryan97@gmail.com')