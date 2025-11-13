#simple version
to_do_list = []

while True:
    print("Tasks:",to_do_list)
    print("Menu")
    print("1. Add\n2. Remove\n3. Exit and Display\n")
    
    userinput = int(input("Enter:"))

    if userinput == 1:
        task = input("Task:")
        to_do_list.append(task)

    elif userinput == 2:
        task = input("Task:")
        if task in to_do_list:
            to_do_list.remove(task)
        else:
            print("Doesn't exist")

    elif userinput == 3:
        print("Tasks:",to_do_list)
        break

    else:
        print("Invalid option")
        




