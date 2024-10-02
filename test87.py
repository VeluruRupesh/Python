# Write program using MAATCH SOFT KEYWORD

cname=input("Enter Course Name: ")
match(cname):
    case "Java":
        print("Java is for developing web applications")
    case "Python":
        print("Pythong is General Purpose Language")
    case "Oracle":
        print("Oracle is used for database")
    case _:
        print("Language Description is not found")
