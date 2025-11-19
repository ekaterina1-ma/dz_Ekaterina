from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
driver = webdriver.Firefox(options=options)

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, 'input')

    input_field.send_keys("Sky")
    time.sleep(1)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("Pro")
    time.sleep(1)

finally:
    driver.quit()
