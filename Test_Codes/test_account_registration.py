from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import registration_data
import pytest


class TestAccountReg:
    url = "https://demo.guru99.com/V4/index.php"

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup and teardown for Selenium WebDriver"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.quit()

    def test_account_reg(self):
        self.driver.get(self.url)

        # Login
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_username).send_keys(
            registration_data.RegistrationData.input_username
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_password).send_keys(
            registration_data.RegistrationData.input_password
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_loginbutton).click()

        # Click en "Nuevo Cliente"
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_new_customer).click()

        # Rellenar formulario
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_customer_name).send_keys(
            registration_data.RegistrationData.input_customer_name
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_gender).click()
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_date_of_birth).send_keys(
            registration_data.RegistrationData.input_dob
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_address).send_keys(
            registration_data.RegistrationData.input_address
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_city).send_keys(
            registration_data.RegistrationData.input_city
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_state).send_keys(
            registration_data.RegistrationData.input_state
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_pin).send_keys(
            registration_data.RegistrationData.input_pin
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_mobile_number).send_keys(
            registration_data.RegistrationData.input_mobile_number
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_email).send_keys(
            registration_data.RegistrationData.input_email
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_password1).send_keys(
            registration_data.RegistrationData.input_password1
        )

        # Enviar formulario
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_submit).click()

        # Validar registro exitoso
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, registration_data.ElementLocators.xpath_of_success))
        )
        assert success_message.text == "Customer Registered Successfully!!!"
        print(f"SUCCESS # CUSTOMER {registration_data.RegistrationData.input_customer_name} REGISTERED SUCCESSFULLY")

        # Obtener ID del cliente generado
        generated_customer_id = self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_generated_id).text

        # Crear nueva cuenta
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_new_account).click()
        
        # Usar el ID generado en lugar del ID estático
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_customer_id).send_keys(
            generated_customer_id  # Changed this line to use the generated ID
        )
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_account_type).click()
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_current_account).click()
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_initial_deposit).send_keys(
            registration_data.AccountData.input_initial_deposit
        )

        # Enviar formulario de cuenta
        self.driver.find_element(By.XPATH, registration_data.ElementLocators.xpath_of_submit1).click()

        # Validar creación de cuenta con espera explícita
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, registration_data.ElementLocators.xpath_of_account_successful))
        )
        assert success_message.text == "Account Generated Successfully!!!"
        print("SUCCESS # ACCOUNT GENERATED SUCCESSFULLY")