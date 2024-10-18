# Login Application

Users_Dict={'Rupesh':'r123',
            'Suresh':'s234',
            'Arun':'a456',
            'Sireesha':'s1020'}
user_name=input('Enter User Name: ')
pwd=input('Enter password: ')
if user_name in Users_Dict:
    password=Users_Dict[user_name]
    if pwd==password:
        print(f'{user_name} Welcome')
    else:
        print('Invalid Password')
else:
    print('Invalid User Name')
