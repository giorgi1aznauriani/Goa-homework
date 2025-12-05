# 1)შექმენით სია სადაც გექნებათ რიცხვები მოცემული და 

# ახალ სიაში ჩაამატეთ ისეთი რიცხვები რომლებიც იყოფა 3ზეც და 5 ზეც

# 2)შექმენით სია სადაც გექნებათ მოცემული სახელები, შემდეგ ახალ სიაში ჩაამატეთ ისეთი სახელები სახელები რომლის სიმბოლოების რაოდენობაც არის ლუწი რიცხვი

# 3) ახსენით კომენტარებით რაში გვჭირდება list comprehension

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 28, 27, 45, 50, 60]
nums = [num for num in list if num % 3 == 0 and num % 5 == 0]
print(nums)


names = ["Giorgi", "Mariami", "Mate", "Nikolozi", "Dato", "Anano", "Ninia", "Saba"]
length_names = [name for name in names if len(name) % 2 == 0]
print(length_names)

# ჩვენ ვიყენებთ list comprehensions კოდის შესამოკლებლად ღონდ როდესაც მარტო for ციკლს,
