# 1. Find the faculty with highest student count who got more than 90%.
import csv

def fac_with_high_student_count(student_marks, faculty_details):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0
    high_marks = {}
    msg = None

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for record in list(data):
            if int(record['Telugu']) >= 90:
                Telugu += 1
            if int(record['English']) >= 90:
                English += 1
            if int(record['Mathematics']) >= 90:
                Maths += 1
            if int(record['Physics']) >= 90:
                Physics += 1
            if int(record['Chemistry']) >= 90:
                Chemistry += 1
            if int(record['Social']) >= 90:
                Social += 1

        high_marks = {
            'Telugu' : Telugu,
            'English' : English,
            'Mathematics' : Maths,
            'Physics' : Physics,
            'Chemistry' : Chemistry,
            'Social' : Social
        }
        
    max_marks = max(high_marks.items(), key = lambda x: x[1])
    print(max_marks)

    with open(faculty_details, 'r') as csvfile:
        faculty_data = list(csv.DictReader(csvfile))
        for i in faculty_data:
            if  max_marks[0] == i['Subject']:
                msg = f'The faculty with highest student count who got more than 90 percent is {i["Faculty"]} and his subject is {i["Subject"]}.'
    return msg

print(fac_with_high_student_count('Assignments/student_marks.csv', 'Assignments/subject_faculty.csv'))

# 2. Find the faculty with highest pass percentage (> 40%)
import csv

def fac_high_pass_percentage(student_marks,subject_faculty):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0
    pass_mark = {}
    msg2 = None

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for marks in data:
            if int(marks['Telugu']) > 40:
                Telugu += 1
            if int(marks['English']) > 40:
                English += 1
            if int(marks['Mathematics']) > 40:
                Maths += 1
            if int(marks['Physics']) > 40:
                Physics += 1
            if int(marks['Chemistry']) > 40:
                Chemistry += 1
            if int(marks['Social']) > 40:
                Social += 1
        
        pass_mark = {
            'Telugu' : Telugu,
            'English' : English,
            'Mathematics' : Maths,
            'Physics' : Physics,
            'Chemistry' : Chemistry,
            'Social' : Social
        }

    pass_perc = max(pass_mark.items(),key=lambda x:x[1])
    print(pass_perc)

    with open(subject_faculty,'r') as csvfile:
        sub_fac = list(csv.DictReader(csvfile))
        for i in sub_fac:
            if pass_perc[0] == i['Subject']:
                msg2 = f"The faculty with highest pass percentage greater than 40% is {i['Faculty']} and his subject is {i['Subject']}."
    return msg2

print(fac_high_pass_percentage('Assignments/student_marks.csv','Assignments/subject_faculty.csv'))

# 3. Find the faculty with least pass percentage (<= 40%)
import csv

def fac_least_pass_percentage(student_marks,subject_faculty):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0

    least_mark = {}
    msg3 = None

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for marks in data:
            if int(marks['Telugu']) <= 40:
                Telugu += 1
            if int(marks['English']) <= 40:
                English += 1
            if int(marks['Mathematics']) <= 40:
                Maths += 1
            if int(marks['Physics']) <= 40:
                Physics += 1
            if int(marks['Chemistry']) <= 40:
                Chemistry += 1
            if int(marks['Social']) <= 40:
                Social += 1
        
        least_mark = {
            'Telugu' : Telugu,
            'English' : English,
            'Mathematics' : Maths,
            'Physics' : Physics,
            'Chemistry' : Chemistry,
            'Social' : Social
        }

    least_pass_perc = max(least_mark.items(),key=lambda x:x[1])
    print(least_pass_perc)

    with open(subject_faculty,'r') as csvfile:
        faculty_data = list(csv.DictReader(csvfile))
        for i in faculty_data:
            if least_pass_perc[0] == i['Subject']:
                msg3 = f"The faculty with least pass percentage with less than or equal to 40% is {i['Faculty']} and his subject is {i['Subject']}."
    return msg3

print(fac_least_pass_percentage('Assignments/student_marks.csv','Assignments/subject_faculty.csv'))

# 4. Who is the top student with maximum total?
import csv

def top_student_max_total(student_marks):
    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Mathematics']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))
            total = sum(marks)
            total_marks[records['studentname']] = total
        students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)
        msg4 = f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}"

    return msg4

print(top_student_max_total('Assignments/student_marks.csv'))

# 5.Who is the best student in Mathematics?
import csv

def top_student_max_subject(student_marks, subject):
    with open(student_marks, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        subject_marks = {}
        for records in data:
            marks = int(records[subject])
            subject_marks[records['studentname']] = marks
        students = sorted(subject_marks.items(), key=lambda x: x[1], reverse=True)
        msg = f"The top student in {subject} is {students[0][0]} with a score of {students[0][1]}"

    return msg

print(top_student_max_subject('Assignments/student_marks.csv', 'Mathematics'))

 # What is the average mark for each subject, (ignore failures)?
import csv

def avg_mark_sub(student_marks):
    telugu_sum = 0; telugu_count = 0
    english_sum = 0; english_count = 0
    maths_sum = 0; maths_count = 0
    physics_sum = 0; physics_count = 0
    chemistry_sum = 0; chemistry_count = 0
    social_sum = 0; social_count = 0

    pass_mark = 40

    avg_marks = {}

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for record in data:
            if int(record['Telugu']) >= pass_mark:
                telugu_sum += int(record['Telugu'])
                telugu_count += 1
            if int(record['English']) >= pass_mark:
                english_sum += int(record['English'])
                english_count += 1
            if int(record['Mathematics']) >= pass_mark:
                maths_sum += int(record['Mathematics'])
                maths_count += 1
            if int(record['Physics']) >= pass_mark:
                physics_sum += int(record['Physics'])
                physics_count += 1
            if int(record['Chemistry']) >= pass_mark:
                chemistry_sum += int(record['Chemistry'])
                chemistry_count += 1
            if int(record['Social']) >= pass_mark:
                social_sum += int(record['Social'])
                social_count += 1

        avg_marks = {
            'Telugu' : telugu_sum/telugu_count,
            'English' : english_sum/english_count,
            'Mathematics' : maths_sum/maths_count,
            'Physics' : physics_sum/physics_count,
            'Chemistry' : chemistry_sum/chemistry_count,
            'Social' : social_sum/social_count
        }

    Subjects = sorted(avg_marks.items(),key = lambda x: x[1],reverse=True)
    print(Subjects)

    msg6 = (f"Ignoring failures,the Average mark for {Subjects[0][0]} is {round(Subjects[0][1])}",
            f"Ignoring failures,the Average mark for {Subjects[1][0]} is {round(Subjects[1][1])}",
            f"Ignoring failures, the Average mark for {Subjects[2][0]} is {round(Subjects[2][1])}",
            f"Ignoring failures,the Average mark for {Subjects[3][0]} is {round(Subjects[3][1])}",
            f"Ignoring failures, the Average mark for {Subjects[4][0]} is {round(Subjects[4][1])}",
            f"Ignoring failures,the Average mark for {Subjects[5][0]} is {round(Subjects[5][1])}")
    
    return msg6
print(avg_mark_sub('Assignments/student_marks.csv'))

#  Find the student with least numbers of marks as total.
import csv

def student_least_marks_totla(student_marks):
    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Mathematics']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))

            total = sum(marks)
            total_marks[records['studentname']] = total
        students = sorted(total_marks.items(), key=lambda x: x[1])
        msg7 = f"The Student is {students[0][0]} and his Least mark is {students[0][1]}"
    
    return msg7
print(student_least_marks_totla('Assignments/student_marks.csv'))