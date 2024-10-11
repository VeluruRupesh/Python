# Write a program to find maximum value from the list

list1=[10,50,20,30,70,80,100,45,78,98,34,65,76,82,89]
m=0
for i in list1:
    if i>m:
        m=i
print(f'List is: {list1}')
print(f'Maximum value is: {m}')

# Find maximum value index
m=0
m_index=None
for i in range(len(list1)):
    if list1[i]> m:
        m_index=i
        m=list1[i]

print(f'List is: {list1}')
print(f'Maximum value index in the list is: {m_index}')
print(f'Maximum value is: {m}')



