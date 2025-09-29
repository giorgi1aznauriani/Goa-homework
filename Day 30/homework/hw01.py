# 2.დაწერე პროგრამა, სადაც დიქშენარში შენახულია პროდუქტების ფასები და დათვალე ჯამური ფასი.

products = {
    "ice cream": 2.5,
    "bread": 1.2,
    "coca-cola": 2.0,
    "milk": 6.5
}

total_price = 0

for price in products.values():
    total_price += price

print("total price:", total_price)


