from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Create a Chrome bot
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

#give key to login form
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)

#click login_button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()
time.sleep(2)
print("login button tested successfully")

#click filter_button
filter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container")))
filter_button.click()
time.sleep(2)
print("filter_button clicked successfully")

#filter_button sort
sort = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[2]")))
sort.click()
time.sleep(2)
print("sorted successfully")

#select the item 
items = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
items.click()
time.sleep(2)
print('item selected')

#item need to add cart
add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
add_to_cart.click()
time.sleep(2)
print('item added cart successfully')

#back to products
back_to_products = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "inventory_details_back_button")))
back_to_products.click()
time.sleep(2)
print('succesfully clicked back_to_products')

#go to cart
Go_to_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
Go_to_cart.click()
time.sleep(2)
print('successfully product added in cart')

#product checkout
checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button")))
checkout.click()
time.sleep(2)
print('product checkout successfully')
 
#sent product delivery address details
driver.find_element(By.ID, "first-name").send_keys("Kalaivanan")
driver.find_element(By.ID, "last-name").send_keys("Pichamuthu")
driver.find_element(By.ID, "postal-code").send_keys("637013")   
print('product delivery details added succesfully')

#delivry address continue button clicked
confirm_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "continue")))
confirm_checkout.click()
time.sleep(2)
print('delivery address continue button clicked')

#delivery confirmrd
finsh = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "finish")))
finsh.click()
time.sleep(2)
print('delivery confirmed successfully')

#back to Products
back_to_Home = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, "back-to-products"))
)
back_to_Home.click()
time.sleep(2)
print('back to products clicked succesfully')

#website tested completed
print("successfully tested")