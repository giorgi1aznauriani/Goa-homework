# 1) შექმენით სტუდენტების სია და გააკეთეთ ყველა მეთოდზე მაგალითი რაც იცით, append,pop,len,find,count

students = ["Giorgi", "Sandro", "Zura", "Nika",]

students.append("Mate")
students.pop(2)

index = students.index("Giorgi")

print(students)
print(index)

print(len(students))

print(students.count("Nika"))

# 2)შექმენით set რომელიც შედგება ხილებისგან და გამოსცადეთ ყველა მეთოდი დღეს რაც ვისწავლეთ

fruits = {"banana", "apple", "pear", "peach"}

fruits.pop()

fruits.discard("pear")

fruits.discard("apple")

fruits.add("watermelon")

print(fruits)




