from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/upload-download")
wait = WebDriverWait(driver, 10)

upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='uploadFile']")))
path = "C:/Users/Usman/Selenium Python Scripts/code.txt"
upload.send_keys(path)
time.sleep(10)
driver.quit()
