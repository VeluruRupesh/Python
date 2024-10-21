def sorted_fun(a,/,*,reversed=False):
    if reversed:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j]<a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]



    else:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]

#main

list1=[1,5,8,2,4,9,3,5,7,10]
print(f'Before sorting {list1}')
sorted_fun(list1)
print(f'After sorting {list1}')
sorted_fun(list1,reversed=True)
print(f'After sorting {list1}')
