# 2.შექმენი სეტი რიცხვებით 1-დან 10-მდე და ამოიღე ყველა ლუწი რიცხვი და ჩასვი სეტში რომელსაც ლისტად გადააქცევთ list ფუნქციის დახმარებით

numbers = set(range(1, 11))
evens = set()

for num in numbers:
    if num % 2 == 0:
        evens.add(num)

even_numbers = list(evens)
print(even_numbers)


