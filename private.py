#private class with both private and public attributes
class PrivateClass:
    def __init__(self):
        #initializing public and private variables
        self.public_data = "public" #public variable
        self.__private_data = "private" #private  variable