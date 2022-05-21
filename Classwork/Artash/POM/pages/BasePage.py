from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class BasePage():
    #def find_elements(self,by_locator):
        #self.browser.find_elements(by_locator)

    def count_elements(self,by_locator):
        all_elements = WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(by_locator))
        return len(all_elements)
    
    def assertion_for_text(self,By_locator,text):
        WebDriverWait(self.browser,10).until(EC.text_to_be_present_in_element(By_locator,text))
        

    def click(self,by_locator):
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(by_locator)).click()
    
    def send_keys(self,by_locator,text_):
        WebDriverWait(self.browser,10).until(EC.presence_of_element_located(by_locator)).send_keys(text_)

