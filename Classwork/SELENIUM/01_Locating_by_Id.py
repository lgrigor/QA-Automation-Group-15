from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://www.facebook.com/")
browser.set_page_load_timeout(60)

#browser.find_element_by_id('email').send_keys('levon.grigoryan97@gmail.com')
email = browser.find_element(By.ID, 'email')
email.send_keys('levon.grigoryan97@gmail.com')

browser.find_element(By.ID, 'pass').send_keys('mypassword')
browser.find_element(By.NAME, 'login').click()

sleep(5)
error_msg = browser.find_element(By.CLASS_NAME, '_9ay7')
assert error_msg.text == "The password you’ve entered is incorrect", "Message"

browser.close()