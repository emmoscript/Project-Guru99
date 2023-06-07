from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import registration_data
import pytest


class TestRegistration():
    url = "https://demo.guru99.com/V4/index.php"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()

    def test_cust_reg(self, launch_driver):
        self.driver.get(self.url)

        # login to webpage
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_username).send_keys(registration_data.RegistrationData.input_username)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_password).send_keys(registration_data.RegistrationData.input_password)

        # click login button
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_loginbutton).click()

        # click new customer tab
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_new_customer).click()

        # click skip ads button
        # frame1 = self.driver.find_element(by=By.ID, value=registration_data.RegistrationData.frame1)
        # self.driver.switch_to.frame(frame1)
        # frame2 = self.driver.find_element(by=By.ID, value=registration_data.RegistrationData.frame2)
        # self.driver.switch_to.frame(frame2)
        # self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_ad_close).click()
        # self.driver.switch_to.default_content()

        # adding customer credentials required
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_customer_name).send_keys(registration_data.RegistrationData.input_customer_name)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_gender).click()
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_date_of_birth).send_keys(registration_data.RegistrationData.input_dob)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_address).send_keys(registration_data.RegistrationData.input_address)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_city).send_keys(registration_data.RegistrationData.input_city)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_state).send_keys(registration_data.RegistrationData.input_state)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_pin).send_keys(registration_data.RegistrationData.input_pin)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_mobile_number).send_keys(registration_data.RegistrationData.input_mobile_number)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_email).send_keys(registration_data.RegistrationData.input_email)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_password1).send_keys(registration_data.RegistrationData.input_password1)

        # click submit
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_submit).click()

        # verify successful customer registration
        result = self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_success)
        response = result.text
        assert response == "Customer Registered Successfully!!!"
        print("SUCCESS # CUSTOMER {customername} REGISTERED SUCCESSFULLY".format(customername=registration_data.RegistrationData.input_customer_name))
       
