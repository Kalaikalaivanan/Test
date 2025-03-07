from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(5)
    assert driver.title == "Google"
    driver.quit

def test_facebook():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    time.sleep(5)
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit

def test_instagram():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.maximize_window()
    time.sleep(5)
    assert driver.title == "Instagram"
    driver.quit



