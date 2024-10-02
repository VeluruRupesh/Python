#Write a program to accept the percentage of user and display grade according to the
#following criteria

#Marks        Grade
#>90            A
#>80 and <=90   B
#>60 and <=80  C
#below 60       D

percentage=int(input("Enter Percentage of Marks: "))

if percentage >90:
    print(f'for {percentage}% student secured Grade A')
elif percentage >80 and percentage <=90:
    print(f'for {percentage}% student secured Grade B')
elif percentage >60 and percentage<=80:
    print(f'for {percentage}% student secured Grade C')
else:
    print(f'for {percentage}% student secured Grade D')
    
