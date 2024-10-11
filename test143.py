# Write a program to read scores of n players and store them in the list
#Calculate total scores

scores=[]

n= int(input("Hoew many players? "))

for i in range(n):
    s=int(input("Enter socre: "))
    scores.append(s)

print(scores)
print(f"Total socres: {sum(scores)}")
