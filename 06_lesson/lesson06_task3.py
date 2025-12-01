import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

third_src = None
timeout = 30
start_time = time.time()

while time.time() - start_time < timeout:
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    loaded_images = [img for img in images if img.get_attribute("src")]

    if len(loaded_images) >= 3:
        try:
            third_src = loaded_images[2].get_attribute("src")
            break
        except Exception as e:
            print(f"Ошибка при получении src: {e}")

if third_src:
    file_name = third_src.split("/")[-1]
    print(f"Имя файла: {file_name}")
else:
    print("Не удалось загрузить как минимум 3 изображения/")

driver.quit()
