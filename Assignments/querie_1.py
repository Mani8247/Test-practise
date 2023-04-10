#Find the faculty with highest student count who got more than 90%.
import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

sub_faculty = {
    'Maths' : 'Murali Krishna',
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Social' : 'Krishna Reddy',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi'}

high_marks = {}

with open('C:/Users/mani kumar/Desktop/test work/Test-practise/Assignments/student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    # print(f'data: {list(data)}')
    for record in list(data):
        if int(record['Telugu']) >= 90:
            Telugu += 1
        if int(record['English']) >= 90:
            English += 1
        if int(record['Maths']) >= 90:
            Maths += 1
        if int(record['Physics']) >= 90:
            Physics += 1
        if int(record['Chemistry']) >= 90:
            Chemistry += 1
        if int(record['Social']) >= 90:
            Social += 1

    high_marks['Telugu'] = Telugu
    high_marks['English'] = English
    high_marks['Maths'] = Maths
    high_marks['Physics'] = Physics
    high_marks['Chemistry'] = Chemistry
    high_marks['Social'] = Social

max_marks = max(high_marks.items(),key = lambda x: x[1])
faculty = (max_marks); (sub,marks) = faculty
print(f"The faculty with highest student count who got more than 90% is {sub_faculty[sub]} and his subject is {sub} with marks as {marks}")
