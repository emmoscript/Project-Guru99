# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class LoginData:
    username1 = "standard_user"
    username2 = "locked_out_user"
    username3 = "problem_user"
    username4 = "performance_glitch_user"
    password = "secret_sauce"
    invalid_password = "password"

class CartData:
    firstname = "Ajay"
    lastname = "Shankar"
    zipcode = "600001"
    product_rate1 = 29.99
    product_rate2 = 49.99
    tax = 6.40

# Python Class for Selenium Selectors
class ElementLocators:
    xpath_username = '//input[@id="user-name"]'
    xpath_password = '//input[@id="password"]'
    xpath_login = '//input[@id="login-button"]'
    xpath_product = '//span[@class="title"]'
    xpath_lockeduser = '//div[@id="login_button_container"]/div/form/div[3]/h3'
    xpath_invalid_login = '//div[@id="login_button_container"]/div/form/div[3]/h3'
    xpath_menu = '//button[@id="react-burger-menu-btn"]'
    xpath_logout = '//a[@id="logout_sidebar_link"]'
    xpath_backpack = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    xpath_jacket = '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    xpath_cart_badge = '//div[@id="shopping_cart_container"]/a/span'
    xpath_cart = '//div[@id="shopping_cart_container"]/a'
    xpath_checkout = '//button[@id="checkout"]'
    xpath_firstname = '//input[@id="first-name"]'
    xpath_lastname = '//input[@id="last-name"]'
    xpath_zipcode = '//input[@id="postal-code"]'
    xpath_continue = '//input[@id="continue"]'
    xpath_total = '//div[@id="checkout_summary_container"]/div/div[2]/div[8]'