"""
• Navigate to https://staging.zoneomics.com
• Create a variable and store “”.
• Create a variable and store “”.
• Click Log in Button in the upper right corner

Enter the email in the email field
• Enter the password in the password field.
• Click Login Button

On Dashboard verify if the login is successful using the variable initially
created.


Part A:
• Enter “222 East 41 Street New York USA” in the search field at the top right
corner of the page.
• Now extract the value from the search field and print it.
• Clear the search field.

Part B:
• Click “See More” On Dashboard, Under Recently Purchased Reports

• Once on Zoning Unlocked Reports Page, check how many records the table
contains and print it on the console.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://staging.zoneomics.com.")
wait = WebDriverWait(driver, 10)
password = ""
email = ""

driver.find_element(By.LINK_TEXT, "Log in").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))).send_keys(email)
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys(password)
element = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

search_field = driver.find_element(By.NAME, "dashboard-header-search")
search_field.send_keys("222 East 41 Street New York USA")
time.sleep(5)

# Extract value
search_value = search_field.get_attribute("value")
print("Extract the search field text", search_value)

# clearing
driver.execute_script("arguments[0].value = '';", search_field)
time.sleep(10)

# after clearing
cleared_value = search_field.get_attribute('value')
print("Search field value after clearing:", cleared_value)

see_more_element = driver.find_element(By.XPATH, "//span[text()='See More']")
driver.execute_script("arguments[0].click();", see_more_element)
time.sleep(5)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "default-table")))
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
print(f"total number of records: {len(rows)}")
time.sleep(5)

driver.quit()
