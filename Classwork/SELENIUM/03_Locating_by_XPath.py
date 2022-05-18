from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(r'C:\Users\Levon Grigoryan\Desktop\here\chromedriver'), options=chrome_options)
browser.get(r"C:\Users\Levon Grigoryan\Documents\QA15\selen\03_page_source.html")

element = browser.find_element(By.XPATH, '//mihatelement[@class=\'unique\']|//urishelement')
print(element.text)

print('-------------------------')

elements_list = browser.find_elements(By.XPATH, '//mihatelement[@class=\'unique\']|//urishelement')
for each_element in elements_list:
    print(each_element.text)

exit(0)