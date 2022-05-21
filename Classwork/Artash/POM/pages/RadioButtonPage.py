from selenium.webdriver.common.by import By
from POM.pages.BasePage import BasePage
import time




class RadioButtonPage(BasePage):
    url_radio = "https://demoqa.com/radio-button"
    yes_button = (By.XPATH,"//label[@for='yesRadio']")
    yes_actual_result = (By.XPATH,'//span[contains(text(),"Yes")]/parent::p')
    yes_expected_result = "You have selected Yes"
    immpressive_radio = (By.XPATH,"//label[@for='impressiveRadio']")
    impressive_actual_result = (By.XPATH,'//span[contains(text(),"Impressive")]/parent::p')
    impressive_expected_result = "You have selected Impressive"
    two_inputs = (By.XPATH,'//input[@class="custom-control-input"]')


    def checking_buttons(self):
        self.click(RadioButtonPage.yes_button)
        self.assertion_for_text(RadioButtonPage.yes_actual_result,RadioButtonPage.yes_expected_result)
        self.click(RadioButtonPage.immpressive_radio)
        #self.find_elements(RadioButtonPage.two_inputs)
        list1 = self.count_elements(RadioButtonPage.two_inputs)
        list1 = list(list1)
        for_assert = len(list1)
        assert for_assert == 2, "wrong"
        
        
        
        

        


