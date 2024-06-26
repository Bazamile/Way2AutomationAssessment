import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddUserPage:
    labelAddUser_xpath = "//h3[@class='ng-binding'][contains(.,'Add User')]"

    label_addUser_xpath = "//h3[contains(.,'Add User')]"
    textbox_FirstName_xpath = "//input[@name='FirstName']"
    textbox_LastName_xpath = "//input[@name='LastName']"
    textbox_UserName_xpath = "//input[@name='UserName']"
    textbox_password_xpath = "// input[ @ type = 'password']"
    customerRadioButton_xpath = "//input[contains(@value,'16')]"
    roleDropdownList_xpath = "//select[@name='RoleId']"
    textbox_email_xpath = "//input[@type='email']"
    Cellphone_xpath = "//input[@name='Mobilephone']"
    save_button = "//button[contains(@ng-click,'save(user)')]"
    username_xpath = "(//td[@ng-repeat='column in columns'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self,firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_FirstName_xpath)))
        element.send_keys(firstname)

    def enterLastName(self,lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_LastName_xpath)))
        element.send_keys(lastname)

    def enterUserName(self,username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_UserName_xpath)))
        element.send_keys(username)

    def enterPassword(self,password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)

    def selectCustomer(self,customer):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.customerRadioButton_xpath)))
        element.click()

    def selectRole(self, role):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.roleDropdownList_xpath)))
        element.click()
        select = Select(element)
        select.select_by_visible_text("Admin")

    def enterEmail(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_email_xpath)))
        element.send_keys(email)

    def enterCellphone(self, cellphone):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Cellphone_xpath)))
        element.send_keys(cellphone)

    def clickSaveButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button)))
        element.click()