# 2)მომხმარებელს შემოატანინე სახელი,თუ მომხმარებლის შემოტანილი სახელი შეიცავს ერთ uppercase ასოს მაინც(for loop გამოიყენეთ)მაშინ დაპრინტე ეს სახელი მთლიანად lowercase ში,სხვა შემთხვევაში დაპრინტე ეს სახელი რომელიც იქნება capitalize 

name = input("Enter your name: ")
uppercase = False
for i in name:
    if i.isupper():  
        uppercase = True
if uppercase:
    print(name.lower())
else:
    print(name.capitalize())
