# სეტი:1.დაწერე პროგრამა, სადაც მომხმარებელი შეიყვანს რამდენიმე სიტყვას და შენ უნდა შეინახო მხოლოდ უნიკალური 

some_words = input("Enter some words: ").split()
unique_words = set(some_words)
print("unique words:", unique_words)
