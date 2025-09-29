# 3.გქონდეს დიქშენარი წიგნების შესახებ (სათაური → ავტორი) და მოძებნე რომელ ავტორს ეკუთვნის კონკრეტული წიგნი.

books_and_authors = {
    "Pinocchio": "Carlo Collodi",
    "Train to pakistan": "Khushwant singh",
    "Godan": "Munshi premchand",
    "Untouchable": "Mulk Raj Anand"
}

title = input("Enter book title: ")
if title in books_and_authors:
    print("author:", books_and_authors[title])
else:
    print("Book not found")


