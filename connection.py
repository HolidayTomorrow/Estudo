









class Connection:
    def __init__(self,host= 'localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        #Setter
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
        
c1 = Connection()
c1.set_user('Luiz')
print(c1.user)