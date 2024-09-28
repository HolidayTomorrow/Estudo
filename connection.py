









class Connection:
    def __init__(self,host= 'localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        #Setter
        self.user = user
        
        
c1 = Connection()
c1.set_user('Luiz')
print(c1.user)