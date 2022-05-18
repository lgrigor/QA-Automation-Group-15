from POM.Pages.AccountPage import AccountPage
from POM.Config.config import TestData
from time import sleep
import pytest

class Test_AccountPage(AccountPage):

    def test_registration_valid_login_password(self, setUp):
        self.browser = setUp
        self.browser.get(AccountPage.URL)
        self.registrate_user(TestData.RANDOM_USERNAME, TestData.RANDOM_PASSWORD)

    def test_registration_invalid_login_password(self, setUp):
        self.browser = setUp
        self.browser.get(AccountPage.URL)
        self.login(TestData.RANDOM_USERNAME, TestData.RANDOM_PASSWORD)
        assert self.check_visibility_of_element(AccountPage.ERROR_MSG), 'ERROR MESSAGE WAS NOT FOUND!'