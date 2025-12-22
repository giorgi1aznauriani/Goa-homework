# )მოცემული სტრიქონების სიიდან ["apple", "banana", "cherry", "date"] შექმენით ახალი სია, სადაც ყველა სიტყვა დიდი ასოებით იქნება დაწერილი.

fruits = ["apple", "banana", "cherry", "date"]
fruits_upper = []
for fruit in fruits:
    fruits_upper.append(fruit.upper())
print(fruits_upper)