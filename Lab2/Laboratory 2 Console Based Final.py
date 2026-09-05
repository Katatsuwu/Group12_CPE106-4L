# Student Information Management System
import json

print("<===== STUDENT INFORMATION MANAGEMENT SYSTEM =====>")

# String
name = input("Enter Student Name (Last Name, First Name): ")
course = input("Enter course (e.g., BS Computer Engineering): ")

# Tuple
year = int(input("Enter Enrollment Year: "))
student_number = int(input("Enter Student Number: "))
student_id = (year, student_number)

# List
print("\n----- Manage Subjects -----\n")

numSub = int(input("Enter number of subjects: "))
subjects = []
print("Enter subject codes (e.g., MATH176):")
for _ in range(numSub):
    subject = input(f"Subject {_ + 1}: ")
    subjects.append(subject)

# Remove extra spaces from subjects
subjects = [subject.strip() for subject in subjects]
subjects.sort() # Sort subjects alphabetically

# Dictionary
student = {
    "Name": name,
    "Course": course,
    "Student ID": student_id,
    "Subjects": subjects
}

# Display Student Information
print("\n<===== STUDENT INFORMATION =====>")
print("Name:", student["Name"])
print("Course:", student["Course"])
print("Student ID:", student["Student ID"])

print("Subjects:")
for subject in student["Subjects"]:
    print("-", subject)

print("<================================>")

# Actually storing dictionary for future import purposes
with open("student_records.json", "r") as file:
    students = json.load(file)

student_name = "student" + str(len(students) + 1)
students[student_name] = student

with open("student_records.json", "w") as file:
    json.dump(students, file, indent=4)