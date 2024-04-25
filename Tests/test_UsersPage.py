import allure
import pytest
from allure_commons.types import AttachmentType
from faker import Faker
from selenium.webdriver.common.by import By

from PageObjects.addUserPage import AddUserPage
from PageObjects.usersPage import UsersPage
from Utils.readProperties import ReadConfig


class Test_001_UsersPage:
    fake = Faker()
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

        self.aup.enterLastName(self.fake.name())
        # self.driver.quit()
