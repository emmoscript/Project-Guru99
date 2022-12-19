# Logging in and add new customer account in guru99 webpage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Pom():
    def guru99_cust_account_reg(self):
        driver = webdriver.Chrome()
        guru99_url = "https://demo.guru99.com/V4/index.php"
        driver.get(guru99_url)
        driver.maximize_window()
        time.sleep(5)

        # login to webpage
        xpath_of_username = '//input[@name="uid"]'
        input_username = driver.find_element(By.XPATH, xpath_of_username)
        input_username.send_keys("mngr463502")

        xpath_of_password = '//input[@name="password"]'
        input_password = driver.find_element(By.XPATH, xpath_of_password)
        input_password.send_keys("UnAtUnE")

        # click login button
        xpath_of_loginbutton = '//input[@name="btnLogin"]'
        click_loginbutton = driver.find_element(By.XPATH, xpath_of_loginbutton)
        click_loginbutton.click()
        time.sleep(8)

        # click new customer tab
        xpath_of_new_customer = '//a[@href="addcustomerpage.php"]'
        click_new_customer = driver.find_element(By.XPATH, xpath_of_new_customer)
        click_new_customer.click()
        time.sleep(8)

        # click skip ads button
        frame1 = driver.find_element(By.ID, "google_ads_iframe_/24132379/INTERSTITIAL_DemoGuru99_0")
        driver.switch_to.frame(frame1)
        frame2 = driver.find_element(By.ID, "ad_iframe")
        driver.switch_to.frame(frame2)
        driver.find_element(By.XPATH, "//div[@id='dismiss-button']/div/span").click()
        driver.switch_to.default_content()
        time.sleep(5)

        # adding customer credentials required
        xpath_of_customer_name = '//input[@name="name"]'
        input_customer_name = driver.find_element(By.XPATH, xpath_of_customer_name)
        input_customer_name.send_keys("Guru")

        xpath_of_gender = '//input[@name="rad1"]'
        input_gender = driver.find_element(By.XPATH, xpath_of_gender)
        input_gender.click()

        xpath_of_date_of_birth = '//input[@id="dob"]'
        input_dob = driver.find_element(By.XPATH, xpath_of_date_of_birth)
        input_dob.send_keys("05011992")

        xpath_of_address = '//textarea[@name="addr"]'
        input_address = driver.find_element(By.XPATH, xpath_of_address)
        input_address.send_keys("25 Main street")

        xpath_of_city = '//input[@name="city"]'
        input_city = driver.find_element(By.XPATH, xpath_of_city)
        input_city.send_keys("Chennai")

        xpath_of_state = '//input[@name="state"]'
        input_state = driver.find_element(By.XPATH, xpath_of_state)
        input_state.send_keys("Tamilnadu")

        xpath_of_pin = '//input[@name="pinno"]'
        input_pin = driver.find_element(By.XPATH, xpath_of_pin)
        input_pin.send_keys("600052")

        xpath_of_mobile_number = '//input[@name="telephoneno"]'
        input_mobile_number  = driver.find_element(By.XPATH, xpath_of_mobile_number)
        input_mobile_number .send_keys("26867856")

        xpath_of_email = '//input[@name="emailid"]'
        input_email = driver.find_element(By.XPATH, xpath_of_email)
        input_email.send_keys("guru@k25.com")

        xpath_of_password1 = '//input[@name="password"]'
        input_password1 = driver.find_element(By.XPATH, xpath_of_password1)
        input_password1.send_keys("basil")
        time.sleep(2)

        # click submit
        xpath_of_submit = '//input[@type="submit"]'
        click_submit = driver.find_element(By.XPATH, xpath_of_submit)
        click_submit.click()
        time.sleep(8)

        # verify successful customer registration
        xpath_of_success = '//td[@colspan="2"]//p[@class="heading3"]'
        result = driver.find_element(By.XPATH, xpath_of_success)
        response = result.text
        if response == "Customer Registered Successfully!!!":
            print(response)
        else:
            print("Not Registered Successfully")

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
test = Pom()
test.guru99_cust_account_reg()