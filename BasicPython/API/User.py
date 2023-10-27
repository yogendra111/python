class User:
    # __name = "Rohan" # global private variable

    def __init__(self, name, password):
        self.__name = name  # instance variable
        self.__password = password

    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password
