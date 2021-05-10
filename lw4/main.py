def show_s_info(s_count, s_list):
    print("Student Information")
    print("ID\t\tName\t\tDoB")
    for i in range(s_count):
        s_list[i].display()

def show_c_info(c_count, c_list):
    print("Course Information")
    print("ID\t\tName\t\tCredit")
    for i in range(c_count):
        c_list[i].display()

def show_mark(s_mark):
    print("Student Mark")
    print("ID\t\tName\t\tCourse\t\tMark\t\tCredit")
    for i in range(len(s_mark)):
        s_mark[i].display()

def show(all_mark):
    for i in range(len(all_mark)):
        show_mark(all_mark[i])

def show_gpa(gpa_list):
    print("Student GPA")
    print("ID\t\tName\t\tGPA")
    for i in range(len(gpa_list)):
        gpa_list[i].display()