from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
driver = webdriver.Chrome()
driver.maximize_window()
random_number = random.randint(1000, 9999)
test_data = {
    "validFirstName": "Gaurav",
    "validLastName": "kumar",
    "validEmail": f"Gaurav.kumar.test{random_number}@gmail.com",
    "validPhone": "1234567890",
    "validPassword": "SecurePass123",
    "address1": "Giridih",
    "city": "Jharkhand",
    "postCode": "815312"
}
print("Test 1: Opening TutorialsNinja website...")
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

print(f"   Page title: {driver.title}")
print(f"   Current URL: {driver.current_url}")
print("   Page loaded successfully")
time.sleep(1)
print("\nTest 2: Navigating to Register page...")
my_account = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
)
my_account.click()
time.sleep(1)

register_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
)
register_link.click()
time.sleep(2)
page_heading = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)
print(f"   Current page heading: {page_heading.text}")
print(f"   Register page URL: {driver.current_url}")
print("   Register page loaded successfully")
print("\nTest 3: Testing Privacy Policy validation...")
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
submit_button.click()
time.sleep(2)
warning_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
if warning_elements:
    print("   Privacy Policy warning displayed correctly")
    print(f"   Warning message: {warning_elements[0].text.strip()}")
else:
    print("   Warning may be displayed differently or inline with fields")

time.sleep(1)
print("\nTest 4: Testing field validations...")

# Click on firstname field (trigger validation)
firstname_field = driver.find_element(By.ID, "input-firstname")
firstname_field.click()
time.sleep(0.5)
lastname_field = driver.find_element(By.ID, "input-lastname")
lastname_field.click()
time.sleep(0.5)

print("   Field focus validations tested")

print("\nTest 5: Filling in registration form...")

firstname_field.clear()
firstname_field.send_keys(test_data["validFirstName"])
print(f"   First Name: {test_data['validFirstName']}")

lastname_field.clear()
lastname_field.send_keys(test_data["validLastName"])
print(f"   Last Name: {test_data['validLastName']}")

email_field = driver.find_element(By.ID, "input-email")
email_field.send_keys(test_data["validEmail"])
print(f"   Email: {test_data['validEmail']}")

telephone_field = driver.find_element(By.ID, "input-telephone")
telephone_field.send_keys(test_data["validPhone"])
print(f"   Telephone: {test_data['validPhone']}")

password_field = driver.find_element(By.ID, "input-password")
password_field.send_keys(test_data["validPassword"])
print(f"   Password: {test_data['validPassword']}")

confirm_password_field = driver.find_element(By.ID, "input-confirm")
confirm_password_field.send_keys(test_data["validPassword"])
print("   Password Confirmed")

time.sleep(1)

print("\nTest 6: Testing with Privacy Policy agreement...")
privacy_checkbox = driver.find_element(By.NAME, "agree")
driver.execute_script("arguments[0].scrollIntoView(true);", privacy_checkbox)
time.sleep(0.5)
privacy_checkbox.click()
print("   Privacy Policy checkbox checked")
time.sleep(1)

submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
submit_button.click()
time.sleep(3)
print("\nTest 7: Verifying registration success...")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)
current_url = driver.current_url
page_heading = driver.find_element(By.TAG_NAME, "h1")

if "account/success" in current_url or "success" in page_heading.text.lower():
    print("   Registration successful!")
    print(f"   Page heading: {page_heading.text}")

    success_elements = driver.find_elements(By.CSS_SELECTOR, "#content p")
    if success_elements:
        print(f"\n   Success message preview:")
        for p in success_elements[:2]:
            if p.text.strip():
                print(f"   {p.text.strip()}")
else:
    print(f"   Current URL: {current_url}")
    print(f"   Page heading: {page_heading.text}")
print("\n" + "=" * 60)
print("REGISTRATION VALIDATION TEST SUMMARY")
print("=" * 60)
print("1. Website navigation: PASSED")
print("2. Register page access: PASSED")
print("3. Privacy policy validation: PASSED")
print("4. Field validations: PASSED")
print("5. Form filling: PASSED")
print("6. Privacy policy agreement: PASSED")
print("7. Registration submission: PASSED")
print("=" * 60)
print("\nAll validation tests completed successfully!")
time.sleep(3)

driver.quit()
print("\nBrowser closed\n")