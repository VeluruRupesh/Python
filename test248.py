# Write a function for login
users={'Rupesh':'r123',
      'Rajesh':'r134',
      'Suresh':'s123',
      'Kamesh':'k123',
      'Srikanth':'s123'}
def login(u,p):
    if u in users and users[u]==p:
        return True
    else:
        return False

#Main
print('******LOGIN********')
uname=input('Enter User Name: ')
password= input('Enter Password: ')
if login(uname,password):
    print(f'{uname} Welcome')
else:
    print('Invalid Username or Password')
        
