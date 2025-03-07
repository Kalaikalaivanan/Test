from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.delete_all_cookies()
    driver.maximize_window()
    time.sleep(5)

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_google_url():
    assert driver.current_url == 'https://www.google.com/'

