from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open first tab
driver.get("https://www.google.com")
time.sleep(5)

# Open new tab
driver.execute_script("window.open('https://www.bing.com', '_blank');")
time.sleep(5)
# Get window handles
tabs = driver.window_handles

# Switch to second tab (index 1)
driver.switch_to.window(tabs[1])
# Perform actions in new tab
time.sleep(2)  # Wait for page load
print(driver.title)  # Print title of the new tab

# Switch back to the first tab
driver.switch_to.window(tabs[0])
print(driver.title)  # Print title of the first tab
time.sleep(2)  # Wait for page load
# Close browser
driver.quit()
