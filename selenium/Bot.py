from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
time.sleep(2)  # Wait for the page to load

# Find the search box and enter a query
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium automation with Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Get and print top search results
results = driver.find_elements("css selector", "h3")
for i, result in enumerate(results[:5]):  # Print top 5 results
    print(f"{i+1}. {result.text}")

time.sleep(30)  # Wait for the user to see
print("Automation complete!")