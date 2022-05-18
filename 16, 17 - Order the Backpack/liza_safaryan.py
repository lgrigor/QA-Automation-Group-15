from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--log-level=3')
opt.add_argument('--start-maximized')

browser = webdriver.Chrome(service=ChromeService(r'C:\Users\Liza\Desktop\web driver\chromedriver.exe'))

"""Write a program that will do the following:

Open the Chrome browser
Enter the URL https://www.saucedemo.com/
Login with the username 'standard_user'
Add to cart "Sauce Labs Backpack"
Go to the basket, checkout
Fill all mandatory fields and process
Finish processing
Close the browser"""

browser.get("https://www.saucedemo.com/")
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(1)
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
sleep(1)
browser.find_element(By.XPATH, "//button[@id='checkout']").click()
sleep(1)
browser.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Liza")
browser.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Safaryan")
browser.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("0031")
sleep(1)
browser.find_element(By.XPATH, "//input[@id='continue']").click()
browser.find_element(By.XPATH, "//button[@id='finish']").click()
sleep(2)
browser.close()