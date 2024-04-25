import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObjects.usersPage import UsersPage
from Utils.readProperties import ReadConfig


class Test_001_UsersPage:
    BaseUrl = ReadConfig().getBaseURL()


    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_user_listTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
        self.driver.maximize_window()
        self.up = UsersPage(self.driver)

        self.driver.quit()