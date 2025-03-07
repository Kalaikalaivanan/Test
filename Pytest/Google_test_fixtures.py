from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('--------setup--------')
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.delete_all_cookies()
    driver.maximize_window()
    time.sleep(5)

    yield
    print('--------Teardown--------')
    driver.quit()

@pytest.mark.usefixtures(init_driver)
def test_google_title(init_driver):
    assert driver.title == 'Google'

@pytest.mark.usefixtures(init_driver)
def test_google_url(init_driver):
    
    assert driver.current_url == 'https://www.google.com/'

