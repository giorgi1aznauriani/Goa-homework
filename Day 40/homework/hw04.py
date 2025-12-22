# 4)მოცემული სიიდან ["cat", "dog", "elephant", "mouse"] შექმენით ახალი სია, რომელიც შეიცავს თითოეული სიტყვის სიგრძეს.

animals = ["cat", "dog", "elephant", "mouse"]
lengh = []

for animal in animals:
    lengh.append(len(animal))

print(lengh)