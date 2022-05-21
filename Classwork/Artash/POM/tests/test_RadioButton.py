from POM.pages.RadioButtonPage import RadioButtonPage
import time
class Test_RadioBbutton(RadioButtonPage):
    def test_buttons(self,setup):
        self.browser = setup
        self.browser.get(RadioButtonPage.url_radio)
        self.checking_buttons()
