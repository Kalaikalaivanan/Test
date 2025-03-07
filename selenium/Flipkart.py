import time
import re
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Flipkart Login Details
FLIPKART_PHONE = "9025388795"

# Step 1: Open Flipkart and Enter Phone Number
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
time.sleep(3)

try:
    driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]").click()
    time.sleep(3)
except:
    pass  # Already on login page

driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']").send_keys(FLIPKART_PHONE, Keys.RETURN)
time.sleep(5)  # Wait for OTP input field

# Step 2: Fetch OTP from Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    return build("gmail", "v1", credentials=flow.run_local_server(port=0))

def fetch_otp(service):
    results = service.users().messages().list(userId="me", q="from:flipkart.com").execute()
    if not results.get("messages"):
        return None
    msg = service.users().messages().get(userId="me", id=results["messages"][0]["id"]).execute()
    body = base64.urlsafe_b64decode(msg["payload"]["body"]["data"]).decode("utf-8")
    return re.search(r'\b\d{6}\b', body).group() if re.search(r'\b\d{6}\b', body) else None

gmail_service = get_gmail_service()
otp = None
for _ in range(5):  # Retry for 5 attempts
    otp = fetch_otp(gmail_service)
    if otp:
        break
    time.sleep(5)

if not otp:
    print("Failed to retrieve OTP")
    driver.quit()
    exit()

print("OTP Retrieved:", otp)

# Step 3: Enter OTP in Flipkart and Submit
driver.find_element(By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys(otp, Keys.RETURN)
time.sleep(5)

print("Login Successful!")
driver.quit()
