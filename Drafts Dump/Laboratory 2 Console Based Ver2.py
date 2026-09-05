# Student Information Management System

print("===== STUDENT INFORMATION MANAGEMENT SYSTEM =====")

# String
name = input("Enter Student Name (Last Name, First Name): ")
course = input("Enter course (e.g., BS Computer Engineering): ")

# Tuple
student_id = tuple(input("Enter Student ID (Year, Number): ").split(","))

# List
numSub = int(input("Enter number of subjects: "))
subjects = []
print("Enter subject codes and names (e.g., MATH176 - Calculus 1):")
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
print("\n===== STUDENT INFORMATION =====")
print("Name:", student["Name"])
print("Course:", student["Course"])
print("Student ID:", student["Student ID"])

print("Subjects:")
for subject in student["Subjects"]:
    print("-", subject)

print("================================")







