
from Class_Lib import SQL_Login

my_login = SQL_Login('Joseph', 'abc123', '10.3.3.169', 'MSSQLServer')

my_login.login()



print(str(my_login))

print(hex(id(my_login)))