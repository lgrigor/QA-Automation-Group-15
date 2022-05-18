from selenium.webdriver.common.by import By
from POM.pages.BasePage import BasePage
from time import sleep

class TextBoxPage(BasePage):
    
    url_Textbox = "https://demoqa.com/text-box"
    user_name = (By.ID,'userName')
    user_email = (By.ID,'userEmail')
    current_adress = (By.ID,'currentAddress')
    perm_adress = (By.ID,'permanentAddress')
    submit_btn = (By.ID,'submit')

    def adress_info(self):
            sleep(3)
            self.send_keys(TextBoxPage.user_name,"Artashes")
            self.click(TextBoxPage.submit_btn)