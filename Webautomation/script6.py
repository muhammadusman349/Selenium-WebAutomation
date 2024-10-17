"""
• Go to https://www.digitaltallycounter.com/
• Make the counter to go to 100.
• Verify that the counter is now at 100

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.digitaltallycounter.com/")
counter_display = driver.find_element(By.ID, "current-count")
increment_button = driver.find_element(By.CSS_SELECTOR, "a[id='button-plus']")

current_value = int(counter_display.text)
clicks_needed = 100 - current_value

# Click the increment button until the counter reaches 100
for _ in range(clicks_needed):
    increment_button.click()
    time.sleep(0.5)

# verify counter reach 100
current_value = int(counter_display.text)
print(f"Counter is now at: {current_value}")
assert current_value == 100, "Counter did not reach 100!"

time.sleep(5)
driver.quit()
