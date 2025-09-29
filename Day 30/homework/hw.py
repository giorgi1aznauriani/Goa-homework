# დიქშენარი:შექმენი სტუდენტების ქულების დიქშენარი (სახელი → ქულა) და იპოვე რომელი სტუდენტი მიიღო ყველაზე მაღალი ქულა.

students_scores = {
    "Giorgi": 99,
    "Mate":  97,
    "Sandro": 74,
    "Nika": 85,
    "Zura": 88, 
}

max_score = 0
for name in students_scores:
    if students_scores[name] > max_score:
        max_score = students_scores[name]
        top_student = name

print("Student with the highest score:", top_student)
print("Highest Score:", max_score)
