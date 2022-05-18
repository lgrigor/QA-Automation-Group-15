from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://ui.vision/demo/webtest/frames/")

target_frame = browser.find_element(By.XPATH, '//frame[@src="frame_1.html"]')
browser.switch_to.frame(target_frame)

sleep(3)
button_to_click = browser.find_element(By.XPATH, "//input[@name='mytext1']")
button_to_click.send_keys('test')

sleep(3)
browser.switch_to.default_content()
frames = browser.find_elements(By.TAG_NAME, 'frame')
print(f"Frames on main page - {len(frames)}")