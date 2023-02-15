from selenium.webdriver.common.by import By

from pageObject.homePage import HomePage


class Register:
    button = (By.LINK_TEXT,"Register")
    first_name = (By.XPATH,"//input[@id='customer.firstName']")
    last_name = (By.XPATH,"//input[@id='customer.lastName']")
    address = (By.XPATH,"//input[@id='customer.address.street']")
    city = (By.XPATH,"//input[@id='customer.address.city']")
    state = (By.XPATH,"//input[@id='customer.address.state']")
    zipcode = (By.XPATH,"//input[@id='customer.address.zipCode']")
    phone = (By.XPATH,"//input[@id='customer.phoneNumber']")
    ssn = (By.XPATH,"//input[@id='customer.ssn']")
    username = (By.XPATH,"//input[@id='customer.username']")
    password = (By.XPATH,"//input[@id='customer.password']")
    re_password = (By.XPATH,"//input[@id='repeatedPassword']")
    reg_button = (By.XPATH,"//input[@class='button']")
    message = (By.XPATH,'//*[@id="rightPanel"]/p')

    def __init__(self, driver):
        self.driver = driver

    def clickButton(self):
        return self.driver.find_element(*Register.button).click()
    def get_firstname(self):
        return self.driver.find_element(*Register.first_name).send_keys("www")
    def get_lastname(self):
        return self.driver.find_element(*Register.last_name).send_keys("www")
    def get_address(self):
        return self.driver.find_element(*Register.address).send_keys("www")
    def get_city(self):
        return self.driver.find_element(*Register.city).send_keys("www")
    def get_state(self):
        return self.driver.find_element(*Register.state).send_keys("www")
    def get_zipcode(self):
        return self.driver.find_element(*Register.zipcode).send_keys("www")
    def get_phone(self):
        return self.driver.find_element(*Register.phone).send_keys("www")
    def get_ssn(self):
        return self.driver.find_element(*Register.ssn).send_keys("www")
    def get_username(self):
        return self.driver.find_element(*Register.username).send_keys("www")
    def get_password(self):
        return self.driver.find_element(*Register.password).send_keys("www")
    def get_rePasword(self):
        return self.driver.find_element(*Register.re_password).send_keys("www")
    def click_registerButton(self):
        return self.driver.find_element(*Register.reg_button).click()
    def get_message(self):
        return self.driver.find_element(*Register.message).text
        #homepage = HomePage(self.driver)

