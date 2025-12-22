#  ვქმნით სიას data სადაც შეივინახავ  მომხმარებლის მონაცემებს
data = []

def register():
    # მომხმარებელს ვაყვანინებთ სახელს და პაროლს
    username = input("Enter your username:")
    password = input("Create a new password:")

    # მონაცემებით ვქმნით ლექსიკონს
    current_user = {
        "name": username,
        "password": password
    }

    # ვნახულობთ არის თუ არა სია ცარიელი
    if len(data) == 0:
        # თუ სია ცარიელია პირველი მომხმარებელია და ვარეგისტრირებთ
        print("Registration successfull!")
        data.append(current_user)
    
    # თუ სიაში უკვე არის ერთი მომხმარებელი მაინც
    elif len(data) > 0:
        # ვიწყებთ არსებული მომხმარებლების გამეორებას
        for i in data:
            # ვამოწმებთ ხომ არ არსებობს უკვე ბაზაში მომხმარებელი იგივე სახელით
            if i["name"] == current_user["name"]:
                print("username already exists!")
                # თუ სახელი დაკავებულია ვთხოვთ ახალის შეყვანას
                username = input("Enter another username again: ")
                current_user["name"] = username
                # ვამატებთ განახლებულ მომხმარებელს (შენიშვნა: აქ მეორე შემოწმება აღარ ხდება)
                data.append(current_user)
                break # ვტეხავთ ციკლს
            else:
                # თუ სახელი ატ არის დაკავებული ვარეგისტრირებთ
                print("Registration successfull!")
                data.append(current_user)
                break # ვაჩერებთ ციკლს რ ადგან იგივე მომხმარებელი ბევრჯერ არ დარეგისტრირდეს

# ფუნქციის გამოძახება სამჯერ 
register()
register()
register()