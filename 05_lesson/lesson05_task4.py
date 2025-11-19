import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


options = Options()
driver = webdriver.Firefox(options=options)

try:

    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    time.sleep(1)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")
    time.sleep(1)

    login_button = (
       driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    )
    login_button.click()
    time.sleep(2)

    message_element = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
    print(message_element.text.strip())

finally:
    driver.quit()
