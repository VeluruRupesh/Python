grade_list=[['Rupesh','A'],
            ['Suresh','B'],
            ['Arun','C'],
            ['Rakesh','A'],
            ['Rajesh','C']]
print(grade_list)
grade_listA=[stud for stud in grade_list if stud[1]=='A']
print(grade_listA)
grade_listB=[stud for stud in grade_list if stud[1]=='B']
print(grade_listB)
grade_listC=[stud for stud in grade_list if stud[1]=='C']
print(grade_listC)
