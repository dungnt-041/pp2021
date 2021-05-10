try:
    all_mark = []
    while True:
        print("'A' : Update student info")
        print("'B' : Update course info")
        print("'X' : Update student marks for the course (require course and student info)")
        print("'Y' : Show student marks of all courses and GPA")
        print("'Z' : Exit")
        answer = input("Choose your action : ")
        if answer == "A":
            print()
            s_count = student_count()
            print()
            s_list = student_info(s_count)
            print()
            show_s_info(s_count, s_list)
            print()
        elif answer == "B":
            print()
            c_count = course_count()
            print()
            c_list = course_info(c_count)
            print()
            show_c_info(c_count, c_list)
            print()
        elif answer == "X":
            print()
            s_mark = student_mark(s_count, s_list, c_count, c_list)
            all_mark.append(s_mark)
            update(all_mark)
            print()
            show_mark(s_mark)
            print()
        elif answer == "Y":
            print()
            show(all_mark)
            print()
            gpa_list = calculate_gpa(s_count, c_count, all_mark)
            show_gpa(gpa_list)
            print()
        elif answer == "Z":
            print("Bravo Six, we're going dark !.... ")
            break
        else:
            print()
            print("Action not recognized")
            print()
            continue
except:
    print("An error occurred !")