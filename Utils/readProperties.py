import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():

    @staticmethod
    def getBaseURL():
        BaseUrl = config.get('WebTable', 'BaseUrl')
        return BaseUrl

    @staticmethod
    def getFirstName():
        FirstName = config.get('Users', 'FirstName')
        return FirstName

    @staticmethod
    def getLastName():
        LastName = config.get('Users', 'LastName')
        return LastName

    @staticmethod
    def getUsername():
        Username = config.get('Users', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('Users', 'Password')
        return Password

    @staticmethod
    def getCustomer():
        Customer = config.get('Users', 'Customer')
        return Customer

    @staticmethod
    def getRole():
        Role = config.get('Users', 'Role')
        return Role

    @staticmethod
    def getEmail():
        Email = config.get('Users', 'Email')
        return Email

    @staticmethod
    def getCellphone():
        Cellphone = config.get('Users', 'Cellphone')
        return Cellphone
