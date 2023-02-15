import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from configuration.config import Testdata
from pageObject.homePage import HomePage
from pageObject.open_accountPage import Open_account
from pageObject.registerpage import Register
from utilities.Baseclass import Baseclass


class Test_cust_Login(Baseclass):
    def test_login(self):
        log = self.getlogger()
        self.driver.implicitly_wait(15)
        register = Register(self.driver)
        register.clickButton()
        register.get_firstname()
        register.get_lastname()
        register.get_address()
        register.get_city()
        register.get_state()
        register.get_zipcode()
        register.get_phone()
        register.get_ssn()
        register.get_username()
        register.get_password()
        register.get_rePasword()
        time.sleep(5)
        register.click_registerButton()
        log.info("register completed")
        #assert register.get_message() =="Your account was created successfully. You are now logged in."

        #homepage = HomePage(self.driver)


        #homepage.get_username()
        #self.driver.find_element_by_name("username").send_keys(Testdata.username)

        #homepage.get_password()
        #self.driver.find_element_by_name("password").send_keys(Testdata.password)

        #homepage.click_button()
        #self.driver.find_element_by_css_selector("input.button").click()
        #open_account = Open_account(self.driver)
        # wait = WebDriverWait(self.driver,5)
        # wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Open New Account")))
        #open_account.click_openaccount()
        # self.driver.find_element_by_link_text("Open New Account").click()

        #select1 = Select(open_account.select_dropdown1())
        # select1 = Select(self.driver.find_element_by_xpath("//select[@id='type']"))

        #select1.select_by_visible_text("SAVINGS")

        #select2 = Select(open_account.select_dropdown2())
        # select2 = Select(self.driver.find_element_by_xpath("//select[@id='fromAccountId']"))
        #select2.select_by_visible_text("14787")

        #open_account.click_button()
        # self.driver.find_element_by_css_selector("input.button").click()

        #message = open_account.success_message()
        # message = self.driver.find_element_by_xpath("//p[text()='Congratulations, your account is now open.']")
        #actual_message = "Congratulations, your account is now open."

        #assert open_account.accountId == '15009'
        # assert self.driver.find_element_by_css_selector("a#newAccountId") == '15009'
        #assert message == actual_message



