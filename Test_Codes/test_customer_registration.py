from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import registration_data
import pytest
import time
from datetime import datetime

class TestRegistration():
    url = "https://demo.guru99.com/V4/index.php"
    
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.quit()  # Changed from close() to quit() for cleaner cleanup

    def generate_unique_email(self):
        """Generate a unique email using timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"test{timestamp}@example.com"

    def handle_alert(self, timeout=5):
        """Handle any alerts that appear"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return None

    def test_cust_reg(self, launch_driver):
        self.driver.get(self.url)

        # Login to webpage
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_username).send_keys(
            registration_data.RegistrationData.input_username)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_password).send_keys(
            registration_data.RegistrationData.input_password)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_loginbutton).click()

        # Click new customer tab
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_new_customer).click()

        # Wait for the customer registration form
        wait = WebDriverWait(self.driver, 10)
        customer_name_field = wait.until(
            EC.presence_of_element_located((By.XPATH, registration_data.ElementLocators.xpath_of_customer_name))
        )

        # Adding customer credentials
        customer_name_field.send_keys(registration_data.RegistrationData.input_customer_name)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_gender).click()
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_date_of_birth).send_keys(
            registration_data.RegistrationData.input_dob)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_address).send_keys(
            registration_data.RegistrationData.input_address)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_city).send_keys(
            registration_data.RegistrationData.input_city)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_state).send_keys(
            registration_data.RegistrationData.input_state)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_pin).send_keys(
            registration_data.RegistrationData.input_pin)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_mobile_number).send_keys(
            registration_data.RegistrationData.input_mobile_number)
        
        # Generate and use unique email
        unique_email = self.generate_unique_email()
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_email).send_keys(unique_email)
        
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_password1).send_keys(
            registration_data.RegistrationData.input_password1)

        # Submit form
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_submit).click()

        # Handle any alerts that might appear
        alert_text = self.handle_alert()
        if alert_text:
            print(f"Alert encountered: {alert_text}")
            if "Email Address Already Exist" in alert_text:
                pytest.skip("Email already exists - please try again with a different email")

        # Verify successful registration
        try:
            wait = WebDriverWait(self.driver, 10)
            success_element = wait.until(
                EC.presence_of_element_located((By.XPATH, registration_data.ElementLocators.xpath_of_success))
            )
            response = success_element.text
            assert response == "Customer Registered Successfully!!!"
            print(f"SUCCESS # CUSTOMER {registration_data.RegistrationData.input_customer_name} REGISTERED SUCCESSFULLY")
        except Exception as e:
            print(f"Failed to verify registration success: {str(e)}")
            raise