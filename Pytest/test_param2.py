import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHubspot:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        yield
        self.driver.quit()

    @pytest.mark.parametrize("username,password", [
        ("admin@gmail.com", "admin123"),
        ("naveen@gmail.com", "naveen123"),
        ("kalai@gmail.com", "kalai123")
    ])
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com/login")

        # Handle cookies popup (if any)
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))
            accept_cookies.click()
        except:
            pass

        # Explicitly wait for login container (safe check)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-container")))

        # Instead of By.ID, try CSS selectors (more stable sometimes)
        username_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#username")))
        username_field.send_keys(username)

        password_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#password")))
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "loginBtn")))
        login_button.click()

        # Optional - Wait for dashboard/home page to load (can add validation here)
        self.wait.until(EC.presence_of_element_located((By.ID, "nav-primary-home")))
