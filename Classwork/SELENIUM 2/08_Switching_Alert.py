from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

#time.sleep(2)
browser.find_element(By.ID, "promptexample").click()

alert_obj = browser.switch_to.alert

#time.sleep(2)
print(f"Text in alert - {alert_obj.text}")

#time.sleep(2)
alert_obj.send_keys('Levon Grigoryan')

#time.sleep(2)
#alert_obj.accept()
alert_obj.dismiss()
