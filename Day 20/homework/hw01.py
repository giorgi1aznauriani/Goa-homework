# 2)მომხმარებელს შემოატანინე სახელი,თუ მომხმარებლის შემოტანილი სახელი შეიცავს ერთ uppercase ასოს მაინც(for loop გამოიყენეთ)მაშინ დაპრინტე ეს სახელი მთლიანად lowercase ში,სხვა შემთხვევაში დაპრინტე ეს სახელი რომელიც იქნება capitalize 

name = input("Enter your name: ")
contains_uppercase = False
for i in name:
    if i.isupper():  
        contains_uppercase = True
if contains_uppercase:
    print(name.lower())
else:
    print(name.capitalize())
