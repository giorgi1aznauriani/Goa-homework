# 2) შექმენით ცვლადი რომელშიც შენახული იქნება პინ კოდი მაგ:1234 და მომხმარებელს შემოაყვანინეთ პინ კოდი და შეინახეთ ისიც ცვლადში, სანამ შემოყვანილი პინ-კოდი არ დაემთხვევა ორიგინალ პინ-კოდს მომხმარებელს შემოაყვენინეთ თავიდან   (while ციკლის გამოყენებით)


original_pin = "1234"

while input(" enter your  pincode: ") != original_pin:
    print("Incorrect!")
    
print("correct!")




