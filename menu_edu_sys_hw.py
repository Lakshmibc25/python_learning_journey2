def menu():
    print("--education system--")
    print("1. details")
    print("2. display")
    print("3.exit")

while True:
    menu()
    choice = int(input("enter your choice : "))
    if choice == 1:
        name = input("enter student name:")
        age = input("enter student age: ")
    student_added = [{"Name= name,Age=age"}]
    print("student_added")
    
    elif choice == 2:
     if student:
       for s in student:
        print(f"Name: {s['Name']} , Age:{s['Age']}")

     else:
       print("no students to display")
    elif choice == 3:
      print("exiting...")
     break
    else:
     print("invalid choice,try again")
