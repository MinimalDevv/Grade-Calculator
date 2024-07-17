HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Step 1: Read input and calculate category averages
student_status = input().strip()
if student_status not in ["UG", "G", "DL"]:
    print("Error: student status must be UG, G or DL")
    exit()

homework_points, quiz_points, midterm_score, final_score = map(float, input().split())

# Calculate percentages
homework = (homework_points / HOMEWORK_MAX) * 100
quizzes = (quiz_points / QUIZZES_MAX) * 100
midterm = (midterm_score / MIDTERM_MAX) * 100
final_exam = (final_score / FINAL_MAX) * 100

# Output category averages formatted to one decimal place
print(f"Homework: {homework:.1f}%")
print(f"Quizzes: {quizzes:.1f}%")
print(f"Midterm: {midterm:.1f}%")
print(f"Final Exam: {final_exam:.1f}%")

# Step 2: Cap any average above 100% to 100%
homework = min(homework, 100)
quizzes = min(quizzes, 100)
midterm = min(midterm, 100)
final_exam = min(final_exam, 100)

print()

# Output capped category averages formatted to one decimal place
print(f"Homework: {homework:.1f}%")
print(f"Quizzes: {quizzes:.1f}%")
print(f"Midterm: {midterm:.1f}%")
print(f"Final Exam: {final_exam:.1f}%")

# Step 3: Calculate and output course average based on student status
if student_status == "UG":
    course_average = 0.2 * homework + 0.2 * quizzes + 0.3 * midterm + 0.3 * final_exam
    print(f"UG average: {course_average:.1f}%")
elif student_status == "G":
    course_average = 0.15 * homework + 0.05 * quizzes + 0.35 * midterm + 0.45 * final_exam
    print(f"G average: {course_average:.1f}%")
elif student_status == "DL":
    course_average = 0.05 * homework + 0.05 * quizzes + 0.4 * midterm + 0.5 * final_exam
    print(f"DL average: {course_average:.1f}%")

# Step 4: Determine course letter grade based on course average
if course_average >= 90.0:
    letter_grade = "A"
elif course_average >= 80.0:
    letter_grade = "B"
elif course_average >= 70.0:
    letter_grade = "C"
elif course_average >= 60.0:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Course grade: {letter_grade}")
