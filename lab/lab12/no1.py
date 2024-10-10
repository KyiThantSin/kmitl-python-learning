def phone_book_manager():
    phone_book = {}
    
    while True:
        print("------------")
        print("Phonebook Manager")
        print("Press '+' to add a new contact ")
        print("Press '-' to delete a contact")
        print("Press 'f' to find a contact")
        print("Press 'p' to print out all contacts in the phonebook")
        print("Press 'q' to quite the program")

        choice = input("Enter a key to process: ")
        print("------------")

        if choice == "+":
            name = input("Enter a name: ")
            phoneNo = input("Enter a phone Number: ")
            
            phone_book[name] = phoneNo
            print("Added!!")
        
        if choice == "-":
            name = input("Enter a name u want to delete: ")
            del phone_book[name]
            print("Deleted!")
        
        if choice == "f":
            name = input("Enter a name u want to search: ")
            search_list = {}
            for key in phone_book:
                if key == name:
                    search_list[key] = name
            
            if search_list.__len__() > 0: 
                for key in search_list:
                    print(key,":",str(phone_book[key]))
            else:
                print("No one found")

       
        if choice == "p":
            for key in phone_book:
                print(key,":",str(phone_book[key]))
        
        if choice == "q":
            print("Good Bye!")
            break
            


phone_book_manager()