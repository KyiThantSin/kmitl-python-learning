def name_list():
    user_list = []
    count = 0
    while True:
        user = input(f"Enter name {count} :")
        count = count + 1
        if user != "":
           user_list.append(user)
        else:
            break
    return user_list
    
names = name_list()
print(names)