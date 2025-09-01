# 1) კომენტარებით ახსენით რა განსხვავებაა list სა და tuple ს შორის
# list  არის mutable tuple არის immutable 
# lists შეიძლება დაემატოს შეეცვალოს და ამოეღოს ელემენტები  tuples არ შეუძლია

# 2)შექმენით Tuple რომელიც შედგება 5 ელემენტისგან
names = ("Giorgi", "Mate", "Sandro", "Khvicha", "Zura")

name1,name2,*other_names = names
print(names)
