from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import login_data
import pytest


class TestLogin:
    url = "https://www.saucedemo.com/"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()
    
    def test_login1(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username1, password=login_data.LoginData.password))

    def test_login2(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username2)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        lock = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_lockeduser).text
        assert lock == 'Epic sadface: Sorry, this user has been locked out.'
        print("SUCCESS # USER LOCKED OUT")
              
    def test_login3(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username3)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username3, password=login_data.LoginData.password))

    def test_login4(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username4, password=login_data.LoginData.password))

    def test_invalid_login(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.invalid_password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        invalid = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_invalid_login).text
        assert invalid == 'Epic sadface: Username and password do not match any user in this service'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username1, password=login_data.LoginData.invalid_password))


