data = []


def register():
    username = input("Enter your username:")
    password = input("Create a new password:")

    current_user = {
        "name":username,
        "password":password
    }
    if len(data) == 0:
        print("Registration successfull!")
        data.append(current_user)
    
    elif len(data) > 0:
        for i in data:
            if i["name"] == current_user["name"]:
                print("username already exists!")
                username = input("Enter another username again: ")
            else:
                print("Registration successfull!")
                data.append(current_user)
    print(data)
        

register()