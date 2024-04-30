import allure
import faker
import pytest
from allure_commons.types import AttachmentType
from faker import Faker
from selenium.webdriver.common.by import By

from PageObjects.addUserPage import AddUserPage
from PageObjects.usersPage import UsersPage
from Utils.readProperties import ReadConfig


class Test_001_UsersPage:
    fake = Faker()
    FirstName = fake.name
    LastName = fake.last_name
    UserName = fake.user_name
    Password = fake.password
    Email = fake.email
    Cellphone = fake.phone_number
    BaseUrl = ReadConfig().getBaseURL()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_user_listTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
        self.driver.maximize_window()
        self.up = UsersPage(self.driver)
        self.aup = AddUserPage(self.driver)


        allure.attach(self.driver.get_screenshot_as_png(), name="User List Page", attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH, self.up.columns_headings_firstName_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.up.columns_headings_lastName_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.up.columns_headings_email_xpath).is_displayed()


        allure.attach(self.driver.get_screenshot_as_png(), name="User fields", attachment_type=AttachmentType.PNG)

        self.up.clickAddUserButton()

        self.driver.find_element(By.XPATH, self.aup.labelAddUser_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add User", attachment_type=AttachmentType.PNG)

        self.aup.enterFirstName(self.fake.name())
        self.aup.enterLastName(self.fake.last_name())
        self.aup.enterUserName(self.fake.user_name())
        self.aup.enterPassword(self.fake.password())
        self.aup.selectCustomer(self)
        self.aup.selectRole(self)
        self.aup.enterEmail(self.fake.email())
        self.aup.enterCellphone(self.fake.phone_number())
        self.aup.clickSaveButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="User Added", attachment_type=AttachmentType.PNG)


        # self.driver.quit()
