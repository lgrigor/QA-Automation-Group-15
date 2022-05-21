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
    user_date = (By.XPATH, "//input[contains(@id, 'user')]")

    def adress_info(self):
            sleep(3)
            self.send_keys(TextBoxPage.user_name,"Artashes")
            self.send_keys(TextBoxPage.user_email,"artashes.badalyan@gmail.com")
            self.send_keys(TextBoxPage.current_adress,"USA")
            self.send_keys(TextBoxPage.perm_adress,"russia")
            self.click(TextBoxPage.submit_btn)
            