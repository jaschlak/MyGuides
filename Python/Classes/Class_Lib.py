


class SQL_Login:
    
    def __init__(self, username, password, address, server_name):
        
        self.username = username
        self.password = password
        self.address = address
        self.server_name = server_name
        
        
    def login(self):
        
        print('You are not logged in as:\nUsername: ' + self.username + \
              '\nPassword: ' + self.password + '\nAddress: ' + self.address + \
              '\nServer: ' + self.server_name)