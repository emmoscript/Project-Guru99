from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import registration_data
import pytest
import time


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

    # def test_account_reg(self, launch_driver):
        self.driver.get(self.url)

        # login to webpage
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_username).send_keys(registration_data.RegistrationData.input_username)
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_password).send_keys(registration_data.RegistrationData.input_password)
        time.sleep(5)

        # click login button
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_loginbutton).click()
        time.sleep(8)

        # click new customer tab
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_new_customer).click()
        time.sleep(8)

        # click skip ads button
        # frame1 = self.driver.find_element(by=By.ID, value=registration_data.RegistrationData.frame1)
        # self.driver.switch_to.frame(frame1)
        # frame2 = self.driver.find_element(by=By.ID, value=registration_data.RegistrationData.frame2)
        # self.driver.switch_to.frame(frame2)
        # self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_ad_close).click()
        # self.driver.switch_to.default_content()
        # time.sleep(5)

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
        time.sleep(2)

        # click submit
        self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_submit).click()
        time.sleep(8)

        # verify successful customer registration
        result = self.driver.find_element(by=By.XPATH, value=registration_data.ElementLocators.xpath_of_success)
        response = result.text
        assert response == "Customer Registered Successfully!!!"
        print("SUCCESS # CUSTOMER {customername} REGISTERED SUCCESSFULLY".format(customername=registration_data.RegistrationData.input_customer_name))

        # saving customer id as variable to parse into customer id data required below
        xpath_of_generated_id = '//*[@id="customer"]/tbody/tr[4]/td[2]'
        gen_id = driver.find_element(By.XPATH, xpath_of_generated_id)
        generated_customer_id = gen_id.text

        # adding a new account inside our customer
        # click new account tab
        xpath_of_new_account = '//a[@href="addAccount.php"]'
        click_new_account = driver.find_element(By.XPATH, xpath_of_new_account)
        click_new_account.click()
        time.sleep(5)

        # # click skip ads button
        # frame1 = driver.find_element(By.ID, "google_ads_iframe_/24132379/INTERSTITIAL_DemoGuru99_0")
        # driver.switch_to.frame(frame1)
        # frame2 = driver.find_element(By.ID, "ad_iframe")
        # driver.switch_to.frame(frame2)
        # driver.find_element(By.XPATH, "//div[@id='dismiss-button']/div/span").click()
        # driver.switch_to.default_content()
        # time.sleep(5)

        # adding account credentials required
        xpath_of_customer_id = '//input[@name="cusid"]'
        input_customer_id = driver.find_element(By.XPATH, xpath_of_customer_id)
        input_customer_id.send_keys(generated_customer_id)

        xpath_of_account_type = '//select[@name="selaccount"]'
        input_account_type = driver.find_element(By.XPATH, xpath_of_account_type)
        input_account_type.click()
        xpath_of_current_account = '//option[@value="Current"]'
        input_current_account = driver.find_element(By.XPATH, xpath_of_current_account)
        input_current_account.click()

        xpath_of_initial_deposit = '//input[@name="inideposit"]'
        input_initial_deposit = driver.find_element(By.XPATH, xpath_of_initial_deposit)
        input_initial_deposit.send_keys("600")

        # click submit
        xpath_of_submit = '//input[@name="button2"]'
        click_submit = driver.find_element(By.XPATH, xpath_of_submit)
        click_submit.click()
        time.sleep(8)

        # verify successful customer registration
        xpath_of_account_successful = '//p[@class="heading3"]'
        result = driver.find_element(By.XPATH, xpath_of_account_successful)
        response = result.text
        if response == "Account Generated Successfully!!!":
            print(response)
        else:
            print("Account Not Generated Successfully")

