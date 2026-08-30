#LABACT PART 2 | TKINTER VER.

#Note: Basic base program only, change whatevs you want :)
#UI Only, no systems implemented yet


from tkinter import *

window = Tk()
window.geometry("600x700")
window.title("Student Information Management System")
window.configure(bg='#2B2B2B')

label = Label(window, text="Student Information Management System", font=('Arial',21,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label2 = Label(window, text="", font=('Arial',20,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label3 = Label(window, text="Student Name", font=('Arial',20,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label.pack()
label2.pack()
label3.pack()

entry = Entry()
entry.config(bg='#FFFFFF')
entry.pack()

label4 = Label(window, text="Course", font=('Arial',20,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label4.pack()
entry2 = Entry()
entry2.config(bg='#FFFFFF')
entry2.pack()

label5 = Label(window, text="", font=('Arial',20,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label5.pack()

label6 = Label(window, text="Manage Subjects", font=('Arial',22,'bold'),fg='#FFFFFF', bg='#2B2B2B')
label6.pack()
#siguro checkboxes nalang dito para sa list ng subjects if yun i-proceed sa console-based

window.mainloop()




