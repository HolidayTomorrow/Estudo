







class Connection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self._user = None
        self._password = None
    @property
    def user(self):
        return self._user
    @property    
    def password(self):
        return self._password
    
    @user.setter
    def setUser(self, user):
        self._user = user
        
    @user.getter
    def getUser(self):
        return self._user
        
    @password.setter
    def setPassword(self, password):
        self._password = password
    
    @user.getter
    def getPassword(self):
        return self._password
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    
    
c1 = Connection()
c1.setUser = 'marcelo.rlopes'
c1.setPassword = 'password123'
print(c1.getUser)
print(c1.getPassword)

# class Connection:
#     def __init__(self,host= 'localhost'):
#         self.host = host
#         self.user = None
#         self.password = None
        
#     def set_user(self, user):
#         #Setter
#         self.user = user
        
#     def set_password(self, password):
#         self.password = password
        
#     @classmethod
#     def create_with_auth(cls, user, password):
#         connection = cls()
#         connection.user = user
#         connection.password = password
#         return connection
    
    
    
# c1 = Connection()
# c1.set_user('Luiz')
# print(c1.user)