import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_test():

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        time.sleep(2)

        button_xpath = (
            "//button[contains(concat(' ', normalize-space(@class), ' '), "
            "' btn-primary ')]"
        )
        button = (
            wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        )
        button.click()

        time.sleep(1)
    finally:
        driver.quit()


run_test()
