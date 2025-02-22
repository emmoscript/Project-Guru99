import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, StaleElementReferenceException
from Test_Data.registration_data import RegistrationData, ElementLocators
import time
import os

class TestBalanceEnquiry:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.guru99.com/V4/")
        yield
        self.driver.quit()

    def test_balance_enquiry(self, setup):
        """
        Test Case 2: Balance Enquiry
        1. Login to the application
        2. Navigate to Balance Enquiry page
        3. Enter account number
        4. Submit the form
        5. Verify the balance enquiry result
        """
        try:
            # Login
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, ElementLocators.xpath_of_username))).send_keys(RegistrationData.input_username)
            self.driver.find_element(By.XPATH, ElementLocators.xpath_of_password).send_keys(RegistrationData.input_password)
            self.driver.find_element(By.XPATH, ElementLocators.xpath_of_loginbutton).click()

            # Navigate to Balance Enquiry
            wait.until(EC.element_to_be_clickable((By.XPATH, ElementLocators.xpath_of_balance_enquiry))).click()

            # Handle advertisement if present
            try:
                if len(self.driver.find_elements(By.ID, RegistrationData.frame1)) > 0:
                    self.driver.switch_to.frame(RegistrationData.frame1)
                    if len(self.driver.find_elements(By.ID, RegistrationData.frame2)) > 0:
                        self.driver.switch_to.frame(RegistrationData.frame2)
                        self.driver.find_element(By.XPATH, ElementLocators.xpath_of_ad_close).click()
                    self.driver.switch_to.default_content()
            except:
                pass

            # Enter account number
            account_no = "142761"  # Replace with a valid account number
            account_input = wait.until(EC.presence_of_element_located((By.XPATH, ElementLocators.xpath_of_account_number)))
            account_input.clear()
            account_input.send_keys(account_no)

            # Submit the form
            self.driver.find_element(By.XPATH, ElementLocators.xpath_of_balance_submit).click()

            # Handle alert if present
            try:
                WebDriverWait(self.driver, 2).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert message: {alert_text}")
                alert.accept()
                assert False, f"Test failed: {alert_text}"
            except:
                pass

            # Verify the result with retry logic in case of stale element
            balance_message = None
            for _ in range(3):  # Retry up to 3 times if stale element error occurs
                try:
                    balance_message = wait.until(EC.presence_of_element_located((By.XPATH, ElementLocators.xpath_of_balance_result)))
                    if balance_message.is_displayed():
                        break
                except StaleElementReferenceException:
                    time.sleep(1)

            assert balance_message and "Balance Details" in balance_message.text, "Balance enquiry failed"

        except UnexpectedAlertPresentException as alert_error:
            print(f"Unexpected alert appeared: {alert_error.alert_text}")
            pytest.fail(f"Test failed: Unexpected alert - {alert_error.alert_text}")

        except Exception as e:
            # Create test_results directory if it doesn't exist
            if not os.path.exists('test_results'):
                os.makedirs('test_results')
            
            # Take screenshot on failure
            screenshot_path = os.path.join('test_results', f"balance_enquiry_error_{time.strftime('%Y%m%d_%H%M%S')}.png")
            self.driver.save_screenshot(screenshot_path)
            raise e

if __name__ == "__main__":
    pytest.main(["-v", "--html=test_results/report.html", "--self-contained-html", "test_balance_enquiry.py"])
