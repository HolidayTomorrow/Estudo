class Client:
    def __init__(self, first_name, last_name, id):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
    
class Account:
    def __init__(self, number, client, balance, limit):
        self.number = number
        self.client = client
        self.balance = balance
        self.limit = limit
        
client = Client('joão', 'Oliveira', '1111111111-1')
my_account = Account('123-4', client, 120.0, 1000.0)
print(client._first_name, client._last_name, client._id)
print(my_account.client._first_name, my_account.client._last_name, my_account.client._id, my_account.number, my_account.balance, my_account.limit)