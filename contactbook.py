contactbook = {}

while True:
    print("1.To add contacts.")
    print("2.Edit.")
    print("3.Search.")
    print("4.Delete")
    print("5.Display")
    print("6.Exit")

    userinput = input("Enter:")

    if userinput == "1":
        name = input("Enter name:")
        numb = input("Enter contact number:")
        
        contactbook[name] = numb
    
    elif userinput == "2":
        name = input("Enter name:")
        if name in contactbook:
            numb = input("Enter new contact number:")
            contactbook[name] = numb
        else:
            print("doesn't exist.")
    
    elif userinput == "3":
        name = input("Enter name:")
        if name in contactbook:
            print(contactbook[name])
        else:
            print("doesn't exist.")

    elif userinput == "4":
         name = input("Enter name:")
         if name in contactbook:
            del contactbook[name]
         else:
            print("doesn't exist.")
    
    elif userinput == "5":
        print(contactbook)
        

    elif userinput == "6":
        break

    else:
        print("Invalid")