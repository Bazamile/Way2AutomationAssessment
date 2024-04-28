import allure
import pytest
from allure_commons.types import AttachmentType
#from faker import Faker
from selenium.webdriver.common.by import By

from PageObjects.usersPage import UsersPage
from PageObjects.addUserPage import AddUserPage
from Utils.readProperties import ReadConfig


class Test_001_UsersPage:
    #fake = Faker()
    # name = fake.name().lastname
    BaseUrl = ReadConfig().getBaseURL()
    FirstName = ReadConfig().getFirstName()
    LastName = ReadConfig().getLastName()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()
    # Customer = ReadConfig().getCustomer()
    # Role = ReadConfig().getRole()
    Email = ReadConfig().getEmail()
    Cellphone = ReadConfig().getCellphone()

    @pytest.mark.e2e
    @pytest.mark.AddUserSuccess
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_list(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
        self.driver.maximize_window()
        self.up = UsersPage(self.driver)
        self.aup = AddUserPage(self.driver)

        allure.attach(self.driver.get_screenshot_as_png(), name="Users List Page", attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH, self.up.columns_headings_firstName_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.up.columns_headings_lastName_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.up.columns_headings_email_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Users List Page - verification",attachment_type=AttachmentType.PNG)
        self.up.clickAddUserButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add User Form", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.aup.addUserForm_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add User Form Details", attachment_type=AttachmentType.PNG)

        #self.aup.enterFirstName(self.fake.name())
        # self.aup.enterLastName(self.fake.name())
        #allure.attach(self.driver.get_screenshot_as_png(), name="FirstName", attachment_type=AttachmentType.PNG)

        # self.aup.enterUserName(self.fake.name())
        # self.aup.enterPassword(self.fake.name())
        # self.aup.selectCustomer(self.fake.name())
        # self.aup.selectRole(self.fake.name())
        # self.aup.enterEmail(self.fake.name())
        # self.aup.enterCellphone(self.fake.name())


        self.aup.enterFirstName(self.FirstName)
        self.aup.enterLastName(self.LastName)
        allure.attach(self.driver.get_screenshot_as_png(), name="FullName", attachment_type=AttachmentType.PNG)
        self.aup.enterUserName(self.Username)
        allure.attach(self.driver.get_screenshot_as_png(), name="UserName", attachment_type=AttachmentType.PNG)
        self.aup.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Password", attachment_type=AttachmentType.PNG)
        self.aup.selectCustomer(self)
        allure.attach(self.driver.get_screenshot_as_png(), name="Selected Customer", attachment_type=AttachmentType.PNG)
        self.aup.selectRole(self)
        allure.attach(self.driver.get_screenshot_as_png(), name="Select Role", attachment_type=AttachmentType.PNG)
        self.aup.enterEmail(self.Email)
        self.aup.enterCellphone(self.Cellphone)
        allure.attach(self.driver.get_screenshot_as_png(), name="Cellphone", attachment_type=AttachmentType.PNG)
        self.aup.clickSaveButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="User Saved", attachment_type=AttachmentType.PNG)
        # self.aup.clickCloseButton()
        # allure.attach(self.driver.get_screenshot_as_png(), name="Users List Page", attachment_type=AttachmentType.PNG)



        self.driver.quit()
