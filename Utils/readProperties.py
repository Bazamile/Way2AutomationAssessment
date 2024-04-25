import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():

    @staticmethod
    def getBaseURL():
        BaseUrl = config.get('Login Details', 'BaseUrl')
        return BaseUrl