# Write s program to create contacts directory
# Input : Name and phone number
# Operations: add , delete and update contacts or numbers

contacts={}
while True:
    print("1. Add Contact: ")
    print("2. Update Contact: ")
    print("3. Remove Contact: ")
    print("4. List Contact: ")
    print("5. Search Contact: ")
    print("6. Exit")
    opt=int(input("Enter your option: "))
    if opt==1:
        name=input("Enter Name of the Person: ")
        if name in contacts:
            print(f'{name} exits')
        else:
            pno=int(input("Enter Phone Number: "))
            contacts[name]=pno
            print("Contact Added")
    elif opt==2:
        name=input("Name: ")
        if name in contacts:
            pno=int(input("Enter New Phone Number"))
            contacts[name]=pno
            print("Contact Updated..")
        else:
            print("{name} not exists")
    elif opt==3:
        name=input("Name: ")
        if name in contacts:
            del contacts[name]
            print("Contact Removed..")
        else:
            print(f'{name} not exits')
    elif opt==4:
        for name,pno in contacts.items():
            print(f'{name}--->{pno}')
    elif opt==5:
        name=input("Name: ")
        if name in contacts:
            pno=contacts[name]
            print(f'{name}-->{pno}')
        else:
            print("Contact do not exist.")
    elif opt==6:
        print("Thanks for using contacts App..")
        break
        
