from tkinter.font import names

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddUserPage:
    addUserForm_xpath = "//h3[contains(.,'Add User')]"
    # FirstName_xpath = "//input[@name='FirstName']"
    # LastName_xpath = "//input[@name='LastName']"
    # UserName_xpath = "//input[@name='UserName']"
    # Password_xpath = "// input[ @ type = 'password']"
    # customerRadioButton_xpath = "//label[@class='radio ng-scope ng-binding'][contains(.,'Company AAA')]"
    # roleDropdownList_xpath = "//select[@name='RoleId']"
    # Email_xpath = "//input[@type='email']"
    # Cellphone_xpath = "//input[@name='Mobilephone']"
    # save_button = "//button[contains(@ng-click,'save(user)')]"
    # close_button = "//button[contains(@ng-click,'save(user)')]"

    def __init__(self, driver):
        self.driver = driver

    # def enterFirstName(self, firstname):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.FirstName_xpath)))
    #     element.send_keys(firstname)
    #
    # def enterLastName(self, lastname):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.LastName_xpath)))
    #     element.send_keys(lastname)
    #
    # def enterUserName(self, username):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.UserName_xpath)))
    #     element.send_keys(username)
    #
    # def enterPassword(self, password):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Password_xpath)))
    #     element.send_keys(password)
    #
    # def selectCustomer(self, customer):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.customerRadioButton_xpath)))
    #     element.click()
    #
    # def selectRole(self, role):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.roleDropdownList_xpath)))
    #     element.click()
    #     select = Select(element)
    #     select.select_by_visible_text("Admin")
    #
    # def enterEmail(self, email):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Email_xpath)))
    #     element.send_keys(email)
    #
    # def enterCellphone(self, cellphone):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Cellphone_xpath)))
    #     element.send_keys(cellphone)
    #
    # def clickSaveButton(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button)))
    #     element.click()
    #
    # def clickCloseButton(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.close_button)))
    #     element.click()

