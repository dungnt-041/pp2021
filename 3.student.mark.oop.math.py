import math
import numpy as np
student = []
course = []
mark = []

print("--------------------------------")
print()

class Std_Info():
    def __init__(self, s_ID, s_Name, s_DoB):
        self.s_ID = s_ID
        self.s_Name = s_Name
        self.s_DoB = s_DoB

    def set_s_ID(self, s_ID):
        self.s_ID = s_ID

    def get_ID(self):
        return self.s_ID

    def set_s_Name(self, s_Name):
        self.s_Name = s_Name

    def get_Name(self):
        return self.s_Name

    def set_s_DoB(self, s_DoB):
        self.s_DoB = s_DoB

    def get_DoB(self):
        return self.s_DoB

    print("Student ID: {0};" + "\n" + "Student Name: {1};" + "\n" + "Student DoB: {2}".format(self.s_ID, self.s_Name, self.s_DoB))



class Course_Info():
    def __init__(self, c_ID, c_Name):
        self.c_ID = c_ID
        self.c_Name = c_Name

    print(self.c_ID, self.c_Name)

    def get_c_ID(self):
        return self.c_ID

class mark_Course():

    def __init__(self, s_ID, c_ID):
        self.s_ID = s_ID
        self.c_ID = c_ID

    def setMark(self, M):
        self.M = M

    def show_M(self):
        print(self.M)

def add_Info():
    # Input Student information ##############################
    # Contain:
    #     - ID
    #     - Name
    #     - Date of Birth
    s_Num = int(input("How many students?\n  -> There are: "))
    for i in range(s_Num):
        Std_Info.s_ID = input("      - Student " + str(i + 1) + " ID: ")
        Std_Info.s_Name = input("      - Student " + str(i + 1) + " Name: ")
        Std_Info.s_DoB = ("      - Student " + str(i + 1) + " DoB: ")
        student.append({"Student " + str(i + 1) + " Id": Std_Info.s_ID, "Student " + str(i + 1) + " Name": Std_Info.s_Name, "Student " + str(i + 1) + " DoB": Std_Info.s_DoB})
        print()
        print("-----------------------------------------------------------------")

    # Input Course information ###############################
    # Contain:
    #      - ID
    #      - Name
    c_Num = int(input("How many courses?\n  -> There are: "))
    for i in range(c_Num):
        print("    * Enter information about course " + str(i + 1) + ": ")
        c_ID = input("      - Course " + str(i + 1) +" ID: ")
        c_Name = input("      - Course " + str(i + 1) +" Name: ")
        course.append({"Course " + str(i + 1) + "Id": c_ID, "Course " + str(i + 1) + "Name": c_Name})
        print()
        print("-----------------------------------------------------------------")

# Ss = Std_Info(input("Something"))
# Cc = Course_Info()
# Mm = mark_Course

def show_Student():
    print("Student list: ")
    for Std_Info in student:
        Std_Info.show_Std()
        print(student)

def show_Course():
    print("Course list: ")
    for Course_Info in course:
        print(Course_Info.show_C())
        print(course)

def show_Mark():
    show_Student()
    s_ID = input("Select Student: ")
    for mark_Course in mark:
        if (mark_Course.s_ID == s_ID):
            mark_Course.show_M()

# Show
###
# def show_Student():
#     print(" # Information about students:")
#     print(student)
#     print()

# def show_Course():
#     print(" # Information about courses:")
#     print(course)
#     print()

###

def marking():
    print("-------------------------------")
    print()

    # Input for choosing:
    #      - Student:      ###########################
    show_Student()
    print(" => Select student by ID:")
    s_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    #      - Course:       ###########################
    show_Course()
    print(" => Select course by ID:")
    c_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    # Mark #######################################
    print()
    m = input(" => Enter the mark: ")
    mark.append({"Student ID": s_ID, "Course ID": c_ID, "Mark": m})
    print()

def show_Marks():
    print(" Here is the list of mark")
    print(mark)
    print()

def option():
    # Option: ########################################

    while (True):
        print("Select an option below: ")
        print("    +> 1. Input information about student and course")
        print("    +> 2. Input mark of student and course")
        print("    +> 3. Show information about student")
        print("    +> 4. Show information about course")
        print("    +> 5. Show mark of students in courses")
        print("    +> 0. Type '0' ('zero') to quit")

        choose = input("      => Your option: ")
        if (choose == "0"):
            break
        if (choose == "1"):
            add_Info()
        if (choose == "2"):
            marking()
        if (choose == "3"):
            show_Student()
        if (choose == "4"):
            show_Course()
        if (choose == "5"):
            show_Marks()

# Information()
# # show_Student()
# # show_Course()
# mark_Course()
# show_Marks()
option()
# Std_Info.show_Std(self)