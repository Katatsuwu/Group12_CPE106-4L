#LABACT PART 1 | CONSOLE-BASED VER.

#Note: Basic base program only, change whatevs you want :)

import random

#=====Basic Student Information=====#
name = input("Enter your name: ")
course = input("Enter course: ")


#=====Subject Managenment=====#
print("\n=======MANAGE SUBJECTS=======\n")

subjects = []

numOfSub = int(input("Enter number of subjects: "))

for counter in range(numOfSub):
    subjects.append(input(f"Enter Subject {counter+1}: "))


#=====Student ID Generation======# 
'''Note: Unsure pa ko sa part na to kung 
random ba talaga dapat student number or dapat consistently adding up from 1001'''

year = 2026
studentNumber = random.randint(1000, 9999)

student_id = (year, studentNumber)


#=====Finalized Student Info=====#

student = {
    "Name": name,
    "Course": course,
    "Student ID": student_id,
    "Subjects": subjects
}

print("\n\n=======STUDENT PROFILE=======\n")

print("Name:", student["Name"])
print("Course:", student["Course"])
print("Student ID:", student["Student ID"])
print("\n-----------------------------")
print("Subjects Enrolled:\n")
for subject in student["Subjects"]:
    print(">", subject)



