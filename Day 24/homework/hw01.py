# 3) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს მომხმარებლის სახელსა და ასაკს. ფუნქციამ უნდა დააბრუნოს მსგავსი წინადადება:
# "მომხმარებლის სახელი" is "მომხმარებლის ასაკი" წლის.

def information(name, age):
    return name + " is " + str(age) + " years old."

result = information("Giorgi", 11)
print(result)




