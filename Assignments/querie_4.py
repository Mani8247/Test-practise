#Who is the top student with maximum total?
import csv


with open('C:/Users/mani kumar/Desktop/test work/Test-practise/Assignments/student_marks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    total_marks = {}
    for row in reader:
        marks = (int(row['Telugu']), int(row['English']), int(row['Maths']), int(row['Physics']), int(row['Chemistry']), int(row['Social']))
        total = sum(marks)
        total_marks[row['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)
print(f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}")