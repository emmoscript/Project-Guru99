# This file consists of Test Information like username, password, XPATH etc
# Create separate classes for all data and locators

# Python Class for Username and Password
class RegistrationData:
    input_username = "mngr611159"
    input_password = "EnYdEga"
    input_customer_name = "Raul Maldonado"
    input_dob = "06062001"
    input_address = "Calle Ejemplo"
    input_city = "Casablanca"
    input_state = "Marrakech"
    input_pin = "452156"
    input_mobile_number  = "5678998754"
    input_email = "dfb6ff@fhjf.com"
    input_password1 = "qwerty12345"
    frame1 = "google_ads_iframe_/24132379/INTERSTITIAL_DemoGuru99_0"
    frame2 = "ad_iframe"

class AccountData:
    customer_id = "generated_customer_id"
    input_initial_deposit = "2000"
    account_number = "generated_account_number"

# Python Class for Selenium Selectors
class ElementLocators:
    xpath_of_username = '//input[@name="uid"]'
    xpath_of_password = '//input[@name="password"]'
    xpath_of_loginbutton = '//input[@name="btnLogin"]'
    xpath_of_new_customer = '//a[@href="addcustomerpage.php"]'
    xpath_of_ad_close = "//div[@id='dismiss-button']/div/span"
    xpath_of_customer_name = '//input[@name="name"]'
    xpath_of_gender = '//input[@name="rad1"]'
    xpath_of_date_of_birth = '//input[@id="dob"]'
    xpath_of_address = '//textarea[@name="addr"]'
    xpath_of_city = '//input[@name="city"]'
    xpath_of_state = '//input[@name="state"]'
    xpath_of_pin = '//input[@name="pinno"]'
    xpath_of_mobile_number = '//input[@name="telephoneno"]'
    xpath_of_email = '//input[@name="emailid"]'
    xpath_of_password1 = '//input[@name="password"]'
    xpath_of_submit = '//input[@type="submit"]'
    xpath_of_success = '//td[@colspan="2"]//p[@class="heading3"]'
    xpath_of_generated_id = '//*[@id="customer"]/tbody/tr[4]/td[2]'
    xpath_of_new_account = '//a[@href="addAccount.php"]'
    xpath_of_customer_id = '//input[@name="cusid"]'
    xpath_of_account_type = '//select[@name="selaccount"]'
    xpath_of_current_account = '//option[@value="Current"]'
    xpath_of_initial_deposit = '//input[@name="inideposit"]'
    xpath_of_submit1 = '//input[@name="button2"]'
    xpath_of_account_successful = '//p[@class="heading3"]'
    xpath_of_balance_enquiry = '//a[@href="BalEnqInput.php"]'
    xpath_of_account_number = '//input[@name="accountno"]'
    xpath_of_balance_submit = '//input[@name="AccSubmit"]'
    xpath_of_balance_result = '//td[@colspan="2"]//p[@class="heading3"]'

