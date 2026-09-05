# LABACT PART 2 | TKINTER IMPLEMENTATION
import json
from tkinter import *
from tkinter import messagebox

windowMain = Tk()
windowMain.state("zoomed")
windowMain.title("Student Information Management System")
windowMain.configure(bg='#2B2B2B')

subjects = []
numSub = 0

#=====MAIN SCREEN=====#

title = Label(windowMain, text="Student Information Management System", font=('Arial',30,'bold'), fg="#00B9B9", bg='#2B2B2B')
title.pack(pady=20)

studentNameLb = Label(windowMain, text="Student Name", font=('Arial',20,'bold'), fg='#FFFFFF', bg='#2B2B2B')
studentNameLb.pack(pady=10)
studentEntry = Entry(windowMain, width=30, font=('Arial',16))
studentEntry.config(bg='#FFFFFF')
studentEntry.pack()

courseLb = Label(windowMain, text="Course", font=('Arial',20,'bold'), fg='#FFFFFF', bg='#2B2B2B')
courseLb.pack(pady=10)
courseEntry = Entry(windowMain, width=30, font=('Arial',16))
courseEntry.config(bg='#FFFFFF')
courseEntry.pack()

enrollmentYrLb = Label(windowMain, text="Enrollment Year", font=('Arial',20,'bold'), fg='#FFFFFF', bg='#2B2B2B')
enrollmentYrLb.pack(pady=10)
enrollmentYrEntry = Entry(windowMain, width=30, font=('Arial',16))
enrollmentYrEntry.config(bg='#FFFFFF')
enrollmentYrEntry.pack()

studentNumberLb = Label(windowMain, text="Student Number", font=('Arial',20,'bold'), fg='#FFFFFF', bg='#2B2B2B')
studentNumberLb.pack(pady=10)
studentNumberEntry = Entry(windowMain, width=30, font=('Arial',16))
studentNumberEntry.config(bg='#FFFFFF')
studentNumberEntry.pack()

subjLb = Label(windowMain, text="Number of Subjects to Take", font=('Arial',22,'bold'), fg='#FFFFFF', bg='#2B2B2B')
subjLb.pack(pady=10)
subjEntry = Entry(windowMain, width=30, font=('Arial',16))
subjEntry.config(bg='#FFFFFF')
subjEntry.pack()

proceedBt = Button(windowMain, text="Proceed to Subject Management", font=('Arial',20,'bold'), fg='#FFFFFF', bg='#00B9B9', command=lambda: proceedToSubjectManagement())
proceedBt.pack(pady=60)


#=====FUNCTIONS=====#
def clearScreen():
    for widget in windowMain.winfo_children():
        widget.destroy()

def proceedToSubjectManagement():
    global numSub
    name = studentEntry.get()
    course = courseEntry.get()
    year = enrollmentYrEntry.get()
    studentNumber = studentNumberEntry.get()
    numSub = int(subjEntry.get())

    windowMain.studentName = name
    windowMain.studentCourse = course
    windowMain.studentYear = int(year)
    windowMain.studentNumber = int(studentNumber)

    showSubjectManagement()


#=====SUBJECT MANAGEMENT=====#

def showSubjectManagement():
    clearScreen()
    manageLb = Label(windowMain, text="Manage Subjects", font=('Arial',30,'bold'), fg='#FFFFFF', bg='#2B2B2B')
    manageLb.pack(pady=20)

    addBt = Button(windowMain, text="ADD", font=('Arial',14,'bold'), fg='#FFFFFF', bg='#00B9B9', command=addSubject)
    addBt.pack(pady=10)

    global subjectList
    subjectList = Listbox(windowMain, width=30, height=6, font=('Arial',16), bg='#FFFFFF')
    subjectList.pack(pady=10)

    confirmBt = Button(windowMain, text="CONFIRM", font=('Arial',14,'bold'), fg='#FFFFFF', bg='#00B9B9', command=confirmSubjects)
    confirmBt.pack(pady=20)


#=====ADD SUBJECT=====#

def addSubject():

    addWindow = Toplevel(windowMain)

    addWindow.geometry("500x300")
    addWindow.title("Add Subject")
    addWindow.configure(bg='#2B2B2B')

    addSubjectLb = Label(addWindow, text="Add Subject", font=('Arial',30,'bold'), fg='#FFFFFF', bg='#2B2B2B')
    addSubjectLb.pack(pady=20)

    subjectEntry = Entry(addWindow, width=30, font=('Arial',16), bg='#FFFFFF')
    subjectEntry.pack(pady=10)

    def saveSubject():

        subject = subjectEntry.get().strip()

        if subject == "":
            return

        if len(subjects) >= numSub:
            return

        subjects.append(subject)
        subjects.sort()
        subjectList.delete(0, END)

        for subject in subjects:
            subjectList.insert(END, subject)

        addWindow.destroy()

    addBt = Button(addWindow, text="ADD", font=('Arial',14,'bold'), fg='#FFFFFF', bg='#00B9B9', command=saveSubject)
    addBt.pack(pady=10)


#=====CONFIRM SUBJECTS=====#

def confirmSubjects():

    if len(subjects) != numSub:
        return

    showStudentInformation()


#=====STUDENT INFORMATION=====#

def showStudentInformation():

    clearScreen()

    student_id = (
        windowMain.studentYear,
        windowMain.studentNumber
    )

    student = {
        "Name": windowMain.studentName,
        "Course": windowMain.studentCourse,
        "Student ID": student_id,
        "Subjects": subjects
    }

    with open("student_records.json", "r") as file:
        students = json.load(file)

    student_name = "student" + str(len(students) + 1)

    students[student_name] = student

    with open("student_records.json", "w") as file:
        json.dump(students, file, indent=4)


    #=====DISPLAY STUDENT INFORMATION=====#


    title = Label(windowMain, text="Student Information Management System", font=('Arial',30,'bold'), fg="#00B9B9", bg='#2B2B2B')
    title.pack(pady=20)

    studentInfoLb = Label(windowMain, text="Student Information", font=('Arial',30,'bold'), fg='#FFFFFF', bg='#2B2B2B')
    studentInfoLb.pack(pady=20)

    nameLb = Label(windowMain, text="Name: " + student["Name"], font=('Arial',22), fg='#FFFFFF', bg='#2B2B2B')
    nameLb.pack(pady=5)

    courseLb = Label(windowMain, text="Course: " + student["Course"], font=('Arial',22), fg='#FFFFFF', bg='#2B2B2B')
    courseLb.pack(pady=5)

    studentIdLb = Label(windowMain, text="Student ID: " + str(student["Student ID"]), font=('Arial',22), fg='#FFFFFF', bg='#2B2B2B')
    studentIdLb.pack(pady=5)

    subjectsLb = Label(windowMain, text="Subjects", font=('Arial',22,'bold'), fg='#FFFFFF', bg='#2B2B2B')
    subjectsLb.pack(pady=20)

    subjectList = Listbox(windowMain, width=30, height=6, font=('Arial',18), bg='#181818', fg='#FFFFFF')
    subjectList.pack()
    subjectList.bind("<MouseWheel>", lambda event: subjectList.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    for subject in student["Subjects"]:
        subjectList.insert(END, subject)


windowMain.mainloop()