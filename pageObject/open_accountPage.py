from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
# open  new account page

class Open_account:
    new_account = (By.LINK_TEXT,"Open New Account")
    dropdown1 = (By.XPATH,"//select[@id='type']")
    dropdown2 = (By.XPATH,"//select[@id='fromAccountId']")
    button = (By.CSS_SELECTOR,"input.button")
    success = (By.XPATH,"//p[text()='Congratulations, your account is now open.']")
    accountId = (By.CSS_SELECTOR,"a#newAccountId")

    def __init__(self,driver):
        self.driver = driver

    def click_openaccount(self):
        return self.driver.find_element(*Open_account.new_account).click()
    def select_dropdown1(self):
        return self.driver.find_element(*Open_account.dropdown1)
    def select_dropdown2(self):
        return self.driver.find_element(*Open_account.dropdown2)
    def click_button(self):
        return self.driver.find_element(*Open_account.button).click()
    def success_message(self):
        return self.driver.find_element(*Open_account.success)
    def account_Id(self):
        return self.driver.find_element(*Open_account.accountId)

