def print_data(*values): 
    for value in values:  
        print(value)









t1=(10,20,30,40,50)
print_data(t1) # value =((10,20,30,40,50)) - it is sending one tuple 
print_data(*t1) # value =((10,20,30,40,50)) - it is sending tuple values
list1=[100,200,300,400,500]
print_data(list1)
print_data(*list1)
