from selenium.webdriver.common.by import By
from POM.Pages.BasePage import BasePage
from POM.Config.config import TestData
from time import sleep

class AccountPage(BasePage):

    URL = 'http://practice.automationtesting.in/my-account/'
    
    ERROR_MSG = (By.XPATH, "//strong[text()='Error:']/..")
    
    #LOCATORS
    LOGIN_EMAIL = (By.XPATH, '//input[@id="username"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@name="login"]')

    REG_EMAIL = (By.XPATH, '//input[@id="reg_email"]')
    REG_PASSWORD = (By.XPATH, '//input[@id="reg_password"]')
    REG_BTN = (By.XPATH, '//input[@name="register"]')

    def login_as_admin(self):
        self.login(TestData.ADMIN_USERNAME, TestData.ADMIN_PASSWORD) 

    def login_as_trader(self):
        self.login(TestData.TRADER_USERNAME, TestData.TRADER_PASSWORD)

    def login(self, username, password):
        self.send_keys(AccountPage.LOGIN_EMAIL, username)
        self.send_keys(AccountPage.LOGIN_PASSWORD, password)
        self.click(AccountPage.LOGIN_BTN)

    def registrate_user(self, username, password):
        """This function is used for registration"""
        sleep(1)
        self.send_keys(AccountPage.REG_EMAIL, username)
        sleep(1)
        self.send_keys(AccountPage.REG_PASSWORD, password)
        sleep(1)
        self.click(AccountPage.REG_BTN)