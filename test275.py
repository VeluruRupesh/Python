# Decorators use case

def box(f):
    def new_display():
        print("*"*50)
        f()
        print("*"*50)
    return new_display


@box   
def display():
    print("Python Language")
@box
def print_data():
    list1={"Rupesh","Rajesh","Rames"}
    for name in list1:
        print(name)

display()
print_data()



#Internal Concept
#new_dis=box(display)
#new_dis()
