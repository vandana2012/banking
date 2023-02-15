
from selenium.webdriver.common.by import By

from configuration.config import Testdata


class HomePage:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    button = (By.CSS_SELECTOR,"input.button")

    def __init__(self,driver):
        self.driver = driver


    def get_username(self):
        return self.driver.find_element(*HomePage.username).send_keys(Testdata.username)

    def get_password(self):
        return self.driver.find_element(*HomePage.password).send_keys(Testdata.password)

    def click_button(self):
        return self.driver.find_element(*HomePage.button).click()