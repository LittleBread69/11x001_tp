"""    
Organise students into the following criteria:
 - Scores 91 - 100: Grade = "Outstanding"
 - Scores 81 - 90: Grade = "Exceeds Expectations"
 - Scores 71 - 80: Grade = "Acceptable"
 - Scores 70 or lower: Grade = "Fail"
 """

 
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,   
}

student_classifications = {}

for student, score in student_scores.items():
    if score > 90:
        student_classifications[student] = "Outstanding"
    elif score > 80:
        student_classifications[student] = "Exceeds Expectations"
    elif score > 70:
        student_classifications[student] = "Acceptable"
    else:
        student_classifications[student] = "Fail"

print(student_classifications)