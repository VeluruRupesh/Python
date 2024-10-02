#logic for withdraw amount from bank

accnot=int(input("Enter Account No: "))
balance=float(input("Balance: "))
ttype=input("D/W: ")
amt=float(input("Amount: "))

if ttype=="W":
    if amt<balance:
        balance=balance-amt
    else:
        print("Insufficient Balance")
elif ttype=="D":
    balance=balance+amt
else:
    print("Invalid Tranaction Type.")

print(f"Avaliable Balance is: {balance:.2f}")
    
    
        
    
