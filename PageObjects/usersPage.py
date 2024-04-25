class UsersPage:
    columns_headings_firstName_xpath = "//span[contains(.,'First Name')]"
    columns_headings_lastName_xpath = "//span[contains(.,'Last Name')]"
    columns_headings_email_xpath = "//span[contains(.,'E-mail')]"

    def __init__(self, driver):
        self.driver = driver
