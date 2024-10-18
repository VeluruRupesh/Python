email_dict={'Rupesh':'roope@gmail.com',
            'Suresh':'s@gmail.com',
            'Kiran':'k@hotmail.com',
            'Rakesh':'r@gmail.com'
            }
print(email_dict)

names=email_dict.keys()
print(names)
emailid=email_dict.values()
print(emailid)
email_data=email_dict.items()
print(email_data)


for name in names:
    print(name)
for email_id in emailid:
    print(email_id)
for email_d in email_data:
    print(email_d)


del email_dict['Rakesh']
print(email_data)
print(email_d)
