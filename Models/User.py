
from Models.Db import Db




class User(Db):
    ALL_USERS = []

    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None


    @property
    def age(self, ):

        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("The user is not of legal age.")
        self.__age = age

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, newname):
        split_name = newname.split()

        if len(split_name) < 2:
            raise ValueError("Name must be in format first last  name")
        self.__name = newname

    def create(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name or age not set")
        try:
            self._cursor = self._connection.cursor()
            self._cursor.execute(
                "INSERT INTO users (username, user_age) VALUES (%s, %s)",
                (self.__name, self.__age)
            )
            self._connection.commit()
            self._connection.close()
            print("The user has been successfully added to the database.")
        except Exception as e:
            print("Error while inserting:", e)


        User.ALL_USERS.append([self.__name, self.__age])











