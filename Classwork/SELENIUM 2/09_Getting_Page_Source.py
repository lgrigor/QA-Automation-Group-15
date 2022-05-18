from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

html_dom = browser.page_source
print(type(html_dom))
print(html_dom)