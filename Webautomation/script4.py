"""
• Go to https://demo.automationtesting.in/Alerts.html
• Click “display an alert box”
• Accept the displayed alert.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.ID, "OKTab").click()
time.sleep(5)

alert = driver.switch_to.alert
print("alter is triggerd", alert.text)

alert.accept()

time.sleep(10)
driver.quit()
