import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.parametrize("username", ["standard_user","locked_out_user","problem_user","performance_glitch_user"])
def test_allUsers(setUp, username, password="secret_sauce"):
    browser: webdriver.Chrome
    browser = setUp
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

def test_urish(setUp):
    browser: webdriver.Chrome
    browser = setUp
    browser.get('https://www.saucedemo.com/')

