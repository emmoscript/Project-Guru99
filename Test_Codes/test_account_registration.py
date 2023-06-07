from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import registration_data
import pytest


class TestAccountReg():
    url = "https://demo.guru99.com/V4/index.php"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()

    def test_account_reg(self, launch_driver):
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

        # saving customer id as variable to parse into customer id data required below
        gen_id = self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_generated_id)
        generated_customer_id = gen_id.text

        # adding a new account inside our customer
        # click new account tab
        click_new_account = self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_new_account).click()

        # # click skip ads button
        # frame1 = driver.find_element(By.ID, "google_ads_iframe_/24132379/INTERSTITIAL_DemoGuru99_0")
        # driver.switch_to.frame(frame1)
        # frame2 = driver.find_element(By.ID, "ad_iframe")
        # driver.switch_to.frame(frame2)
        # driver.find_element(By.XPATH, "//div[@id='dismiss-button']/div/span").click()
        # driver.switch_to.default_content()

        # adding account credentials required
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_customer_id).send_keys(registration_data.AccountData.customer_id)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_account_type).click()
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_current_account).click()
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_initial_deposit).send_keys(registration_data.AccountData.input_initial_deposit)

        # click submit
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_submit1).click()

        # verify successful customer registration
        xpath_of_account_successful = '//p[@class="heading3"]'
        result = self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_account_successful)
        response = result.text
        assert response == "Account Generated Successfully!!!"
        print("SUCCESS # ACCOUNT GENERATED SUCCESSFULLY")


