# Filitering data based on the grade
students={1:{'sname':'Rupesh','Grade':'A'},
          2:{'sname':'Suresh','Grade':'B'},
          3:{'sname':'Ramesh','Grade':'C'},
          4:{'sname':'Vijay','Grade':'A'},
          5:{'sname':'Chand','Grade':'C'},
          6:{'sname':'Siva','Grade':'A'}}
print(students)
print()
students_A={rno:a for rno,a in students.items() if a['Grade']=='A'}
students_B={rno:a for rno,a in students.items() if a['Grade']=='B'}
students_C={rno:a for rno,a in students.items() if a['Grade']=='C'}
print(students_A,students_B,students_C,sep='\n')
