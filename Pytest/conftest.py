import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()  # Or Edge/Firefox based on what you're using
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
