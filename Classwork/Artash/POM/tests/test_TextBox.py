from POM.pages.TextBoxPage import  TextBoxPage
from time import sleep


class Test_textBoxPage(TextBoxPage):
    def test_registration_valid_login_password(self,setup):
        self.browser = setup
        self.browser.get(TextBoxPage.url_Textbox)  
        #self.adress_info()
        #//input[contains(@id, 'user')]
        a = self.count_elements(TextBoxPage.user_date)
        assert a != 2, f'total number of elements are: {a}'
            
        sleep(10)


