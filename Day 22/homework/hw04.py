# 5) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის მეთოდი, რომელიც ისწავლეთ. თითოეულს მიუწერეთ დეტალური განმარტება და მათზე მოიყვანეთ თითო-თითო მაგალითი.

# upper ფუნქციას სიტყვა დიდ ასოებად გადაყავს.
name = "giorgi"
print(name.upper())

# lower ფუნქცია სიტყვას დიდ ასოებად გარდაქმნის.
name = "SANDRO"
print(name.lower())

# capitalize ფუნქციას სიტყვის პირველი ასო გადაყავს დიდად.
name = "apple"
print(name.capitalize())

# find ფუნქციას სიტყვის რომელიმე ასოს ინდექსის გაგება შეუძლია.
word = "grape"
print(word.find("a"))

# isupper ფუნქცია ამოწმებს თუ სიტყვა შედგება დიდ ასოებისგან.
name = "Giga"
print(name.isupper())

# islower ფუნქცია ამოწმებს თუ ცვლადის მნიშვნელობა შედგება პატარა ასოებისგან.
word = "computer"
print(word.islower())

# isalpha ფუნქცია ამოწმებს თუ ცვლადის მნიშვნელობა შედგება ანბანის ასოებისგან.
name = "giorgi12345"
print(name.isalpha())

# isdigit ამოწმებს თუ მხოლოდ რიცხვებისგან შედგება ცვლადის მნიშვნელობა
name =  "156789876543456789"
print(name.isdigit())

# sprit ყოფს ცვლადის მნიშვნელობას
text = "mate,gio,sandro"
print(text.split())

# isalnum ფუნქცია ამოწმებს თუ ცვლადის მნისვნელობა შედგება ანბანის ასოებისგან ან  რიცხვებისგან
name = "gio456789287"
print(name.isalnum())

