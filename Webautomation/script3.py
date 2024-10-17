"""
• Go to https://www.globalsqa.com/demo-site/select-dropdown-menu/
• Change the dropdown value to “Pakistan”
• Verify if the dropdown value is changed to “Pakistan” successfully

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

dropdown = driver.find_element(By.CSS_SELECTOR, "div div p select option[value='PAK']")
dropdown.click()
value = dropdown.text
print(value)

time.sleep(10)
driver.quit()
