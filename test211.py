# Write a program to read scores of n players store in dictionary

players={}
n=int(input("Enter how many players. "))
for i in range(n):
    pname=input("Enter Player Name: ")
    pscore=int(input("Enter Player Score: "))
    players[pname]=pscore

total=0
for pname,pscore in players.items():
    print(f'{pname}\t{pscore}')
    total=total+pscore
print(f'Total Socre: {total}')    
