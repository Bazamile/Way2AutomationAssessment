import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddUserPage:
    labelAddUser_xpath = "//h3[@class='ng-binding'][contains(.,'Add User')]"

    label_addUser_xpath = "//h3[contains(.,'Add User')]"
    textbox_FirstName_xpath = "//input[@name='FirstName']"
    textbox_LastName_xpath = "//input[@name='LastName']"
    textbox_UserName_xpath = "//input[@name='UserName']"
    textbox_password_xpath = "// input[ @ type = 'password']"
    # // input[contains( @ value, '16')]
    # // select[ @ name = 'RoleId']
    textbox_email_xpath = "//input[@type='email']"
    textbox_Mobilephone_xpath = "//input[@name='Mobilephone']"

    def __init__(self, driver):
        self.driver = driver

    def enterLastName(self,lastName):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_LastName_xpath)))
        element.send_keys(lastName)
