from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

#chrome_options = Options()
#chrome_options.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(r'C:\Users\Levon Grigoryan\Desktop\here\chromedriver'))
browser.get(r"C:\Users\Levon Grigoryan\Documents\QA15\selen\07_page_source.html")

# Scenario 1
# username = browser.find_element_by_xpath("/html/body/form/input[1]")
# username = browser.find_element_by_xpath("//input")
# username = browser.find_element_by_xpath("//input[@name='username']")
# username = browser.find_element_by_xpath("//form/input[@name='username']")
# username = browser.find_element_by_xpath("//form[@id='loginForm']/input[1]")

#username = browser.find_element_by_css_selector("html > body > form > input:nth-of-type(1)")
#username = browser.find_element_by_css_selector("input")
#username = browser.find_element_by_css_selector("input[name='username']")
#username = browser.find_element_by_css_selector("form > input[name='password']")
username = browser.find_element_by_css_selector("form#loginForm > input")

username.send_keys('levon.grigoryan97@gmail.com')
exit(0)

# Scenario 2
# clear_button = browser.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
# clear_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")

clear_button = browser.find_element(By.CSS_SELECTOR, "input[name='continue'][type='button']")
clear_button = browser.find_element(By.CSS_SELECTOR, "form[id='loginForm'] > input:nth-of-type(4)")

clear_button.click()
exit(0)