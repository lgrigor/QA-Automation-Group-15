from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():

    

    def click(self,by_locator):
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(by_locator)).click()
    
    def send_keys(self,by_locator,text):
        WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(by_locator)).send_keys(text)

