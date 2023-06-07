# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class RegistrationData:
    input_username = "mngr507659"
    input_password = "sAdebed"
    input_customer_name = "Guru"
    input_dob = "05011992"
    input_address = "25 Main street"
    input_city = "Chennai"
    input_state = "Tamilnadu"
    input_pin = "600052"
    input_mobile_number  = "26867856"
    input_email = "guru@k516.com"
    input_password1 = "basil"
    frame1 = "google_ads_iframe_/24132379/INTERSTITIAL_DemoGuru99_0"
    frame2 = "ad_iframe"

class AccountData:
    firstname = "Ajay"
    lastname = "Shankar"


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
