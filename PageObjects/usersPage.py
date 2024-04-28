import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UsersPage:
    userList_xpath = "//td[@class='smart-table-global-search']"
    columns_headings_firstName_xpath = "//span[contains(.,'First Name')]"
    columns_headings_lastName_xpath = "//span[contains(.,'Last Name')]"
    columns_headings_email_xpath = "//span[contains(.,'E-mail')]"
    addUser_button = "//button[contains(.,'Add User')]"

    def __init__(self, driver):
        self.driver = driver

    def clickAddUserButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.addUser_button)))
        element.click()
