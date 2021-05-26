import pickle
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import math
import datetime
from Domains.Manager import Manager             # Import class Manager
from Domains.Staff import Staff                 # Import class Staff
from Domains.Salary import Salary               # Import class Salary

def check_gender(gender):
    if gender == "Male" or gender == "Female":
        judgment = True                         # If gender is input correctly, return True
    else:
        judgment = False                        # Else return False
    return judgment                             

def prevent_duplicate(id, list):                
    id = id.strip()
    if any(obj.id == id for obj in list):
        judgment = False                        # If ID already existed, return False
    else:
        judgment = True                         # Else return True
    return judgment 

def prevent_duplicate2(office, list):           # For Staff only
    if any(obj.office == office for obj in list):
        judgment = False                        # If office already existed, return False
    else:
        judgment = True                         # Else return True
    return judgment

def add_staff(id, name, gender, DoB, password, frame, window_m):                        # Add Staff info to s_list
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")    # Read Staff_s.pickle
        s_list = pickle.load(f)
        f.close()
    except:
        s_list =[]                                                                      # Create new list if no data
    if prevent_duplicate(id.get(), s_list) == False:
        messagebox.showerror("", "ID already existed !", parent = window_m)             # Show error dialog
    elif id.get() == "Alpha":
        messagebox.showerror("", "Staff ID cannot be Alpha !", parent = window_m)             # Show error dialog
    else:
        office = id.get()[0]
        office = office.upper()
        if prevent_duplicate2(office, s_list) == False:
            messagebox.showerror("", "There cannot be 2 staff in the same office !", parent = window_m) # Error dialog
        else:
            if check_gender(gender.get()) == False:
                messagebox.showerror("", "Gender input Male or Female only !", parent = window_m)       # Error dialog
            else:
                try:
                    birthday = DoB.get()
                    birthday = birthday.split("/" , 2)
                    x = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
                    birthday = (datetime.date.strftime(x, "%d/%m/%Y"))                  # Show DoB in form DD/MM/YYYY
                    s_list.append(Staff(id.get(), name.get(), gender.get(), birthday, office, password.get()))
                    s_list = sorted(s_list, key = lambda x: x.id)                       # Sort s_list base on ID
                    id.delete(0, END)
                    name.delete(0, END)
                    gender.delete(0, END)
                    DoB.delete(0, END)
                    password.delete(0, END)                                             # Clear input fields
                except:
                    messagebox.showerror("", "DoB must be in form (DD/MM/YYYY) !", parent = window_m)   # Error dialog
                if len(s_list) > 7 :
                    messagebox.showwarning("", "No more than 7 Staff !", parent = window_m)             # Error dialog
                else:
                    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "wb")        # Create new Staff_s.pickle
                    pickle.dump(s_list, f)                                                              # Dump s_list to Staff_s.pickle
                    f.close()
                    for i in range(len(s_list)):
                        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(s_list[i].office), "wb")
                        pickle.dump(s_list[i], f)                                                       # Divide Staffs in s_list base on staff.office
                        f.close()                                                                       # Dump each Staff to according file
                    show_staff(frame, window_m)                                                                   # Show s_list

def del_staff(del_id, frame, window_m):                                                 # Del Staff info in s_list
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")        # Read Staff_s.pickle
    s_list = pickle.load(f)
    f.close()
    if not any(staff.id == del_id.get() for staff in s_list):
        messagebox.showerror("", "ID Not Found !", parent = window_m)                   # Error diaglog
    else:
        for i in range(len(s_list)):                                                    # If ID input is found in s_list  
            if s_list[i - 1].id == del_id.get():
                s_list.pop(i - 1)                                                       # Delete the Staff having that ID
        s_list = sorted(s_list, key = lambda x: x.id)
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "wb")    # Create new Staff_s.pickle
        pickle.dump(s_list, f)                                                          # Dump s_list to Staff_s.pickle
        f.close()
        os.remove("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(del_id.get()[0]))    # Delete database file of that Staff
        del_id.delete(0, END)
        for i in range(len(s_list)):
            f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(s_list[i].office), "wb")
            pickle.dump(s_list[i], f)           # Divide Staff in s_list base on ID, dump Staff in according file
            f.close()                           
        show_staff(frame, window_m)                       # Show s_list
    
def show_staff(frame, window_m):                # Show s_list
    for widget in frame.winfo_children():       
       widget.destroy()                         # Reset frame
    frame_label1 = Label(frame, text = "ID")
    frame_label1.grid(row = 0, column = 0)
    frame_label2 = Label(frame, text = "Name")
    frame_label2.grid(row = 0, column = 1)
    frame_label3 = Label(frame, text = "Gender")
    frame_label3.grid(row = 0, column = 2)
    frame_label4 = Label(frame, text = "DoB")
    frame_label4.grid(row = 0, column = 3)
    frame_label5 = Label(frame, text = "Office")
    frame_label5.grid(row = 0, column = 4)
    frame_label6 = Label(frame, text = "Password")
    frame_label6.grid(row = 0, column = 5)
    s_list = []
    try:
        for i in range(ord('A'), ord('Z') + 1):     # i run from A to Z
            try:
                f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(chr(i)), "rb")
                staff = pickle.load(f)
                f.close()
                s_list.append(staff)
            except:
                continue                            # s_list = list of Staff
        for i in range(len(s_list)):
            frame_label1 = Label(frame, text = "{}".format(s_list[i].id))
            frame_label1.grid(row = i + 1, column = 0)
            frame_label2 = Label(frame, text = "{}".format(s_list[i].name))
            frame_label2.grid(row = i + 1, column = 1)
            frame_label3 = Label(frame, text = "{}".format(s_list[i].gender))
            frame_label3.grid(row = i + 1, column = 2)
            frame_label4 = Label(frame, text = "{}".format(s_list[i].DoB))
            frame_label4.grid(row = i + 1, column = 3)
            frame_label5 = Label(frame, text = "{}".format(s_list[i].office))
            frame_label5.grid(row = i + 1, column = 4)
            frame_label6 = Label(frame, text = "{}".format(s_list[i].password))
            frame_label6.grid(row = i + 1, column = 5)
    except:
        messagebox.showwarning("", "No Staff Info exist.\nPlease add Staff Info !", parent = window_m)  # Error dialog

def update_all_staff_salary(working_hour, wage, frame, window_m):                   # Update all staff salary for staff in s_list
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")    # Read Staff_s.pickle
    s_list = pickle.load(f)
    f.close()
    m_list = [] 
    try: 
        if float(working_hour.get()) > 200.0:
            messagebox.showwarning("", "Work Hour : No more than 200h", parent = window_m)          # Error dialog
        else:
            working_hour2 = float(working_hour.get())                               # Turn string to float
            try: 
                if float(wage.get()) > 9999.0:
                    messagebox.showwarning("", "Wage : No more than 9999$ !", parent = window_m)    # Error dialog
                else:
                    for i in range(len(s_list)):
                        wage2 = float(wage.get())                                   # Turn string to float
                        total = wage2 * working_hour2
                        total = math.floor(total)
                        id = s_list[i].id
                        name = s_list[i].name
                        office = id[0]                                              # office =  first letter of ID
                        m_list.append(Salary(id, name, office, working_hour2, wage2, total))
                    m_list = sorted(m_list, key = lambda x: x.id)                   # Sort m_list base on ID
                    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff Salary.pickle", "wb")  
                    pickle.dump(m_list, f)                                          # Create new file, dump m_list to the file
                    f.close()
                    show_all_staff_salary(frame, window_m)                                    # Show m_list
            except:
                    messagebox.showwarning("", "Wage : Number only ! ", parent = window_m)          # Error dialog 
    except:
        messagebox.showwarning("", "Work Hour : Number only !", parent = window_m)                  # Error dialog 
            
def show_all_staff_salary(frame, window_m):         # Show m_list 
    for widget in frame.winfo_children():           # Reset frame
        widget.destroy()
    frame_label1 = Label(frame, text = "ID")
    frame_label1.grid(row = 0, column = 0)
    frame_label2 = Label(frame, text = "Name")
    frame_label2.grid(row = 0, column = 1)
    frame_label3 = Label(frame, text = "Work Hour")
    frame_label3.grid(row = 0, column = 2)
    frame_label4 = Label(frame, text = "Wage/Hour")
    frame_label4.grid(row = 0, column = 3)
    frame_label5 = Label(frame, text = "Office")
    frame_label5.grid(row = 0, column = 4)
    frame_label6 = Label(frame, text = "Salary")
    frame_label6.grid(row = 0, column = 5)
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff Salary.pickle", "rb")      # Read Staff Salary
        m_list = pickle.load(f)
        f.close()
        for i in range(len(m_list)):
            frame_label1 = Label(frame, text = "{}".format(m_list[i].id))
            frame_label1.grid(row = i + 1, column = 0)
            frame_label2 = Label(frame, text = "{}".format(m_list[i].name))
            frame_label2.grid(row = i + 1, column = 1)
            frame_label3 = Label(frame, text = "{}h".format(m_list[i].working_hour))
            frame_label3.grid(row = i + 1, column = 2)
            frame_label4 = Label(frame, text = "{}$".format(m_list[i].wage))
            frame_label4.grid(row = i + 1, column = 3)
            frame_label5 = Label(frame, text = "{}".format(m_list[i].office))
            frame_label5.grid(row = i + 1, column = 4)
            frame_label6 = Label(frame, text = "{}$".format(m_list[i].total))
            frame_label6.grid(row = i + 1, column = 5)
    except:
        messagebox.showwarning("", "No Staff Salary exist.\nPlease update Staff Salary !", parent = window_m)   # Error dialog       

def update_one_staff_salary(id, working_hour, wage, frame, window_m):           # Update salary of one Staff in s_list
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff Salary.pickle", "rb")      # Read database file
        m_list = pickle.load(f)
        f.close()
    except:
        m_list = []
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")                # Read database file
    s_list = pickle.load(f)
    f.close()
    if not any(staff.id == id.get() for staff in s_list):
        messagebox.showerror("", "ID Not Found !", parent = window_m)               # Error dialog 
    else:
        for i in range(len(m_list)):        # If ID is found in m_list
            if m_list[i - 1].id == id.get():
                m_list.pop(i - 1)           # Delete Salary info of that ID
        for i in range(len(s_list)):
            if s_list[i].id == id.get():
                name = s_list[i].name
                office = s_list[i].office
                id2 = id.get()
        try: 
            if float(working_hour.get()) > 200.0:
                messagebox.showwarning("", "Work Hour : No more than 200h")         # Error dialog 
            else:
                working_hour2 = float(working_hour.get())       # String to float
                try: 
                    if float(wage.get()) > 9999.0:
                        messagebox.showwarning("", "Wage : No more than 9999$ !")   # Error dialog 
                    else:
                        wage2 = float(wage.get())               # String to float
                        total = wage2 * working_hour2
                        total = math.floor(total)
                        m_list.append(Salary(id2, name, office, working_hour2, wage2, total))   # Add new salary info for that ID
                        m_list = sorted(m_list, key = lambda x: x.id)
                        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff Salary.pickle", "wb")
                        pickle.dump(m_list, f)      # Dump m_list to new file  
                        f.close()
                        show_all_staff_salary(frame, window_m)    # Show m_list
                except:
                        messagebox.showwarning("", "Wage : Number only ! ", parent = window_m)  # Error dialog 
        except:
            messagebox.showwarning("", "Work Hour : Number only !", parent = window_m)          # Error dialog 

def show_all(window_m):     # Show all employee info and salary
    temp = Toplevel()                           # Create new toplevel window
    temp.title("EMPLOYEES INFO - SALARY")
    temp.grid_rowconfigure(0, weight=1)
    temp.grid_columnconfigure(0, weight=1)      # Set up grid
    temp.resizable(0, 0)                        # Prevent toplevel window to expand

    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")        # Read file
    s_list = pickle.load(f)
    f.close()
    
    frame = LabelFrame(temp, text = "EMPLOYEE INFO")        # Create new frame
    frame.grid(row = 0, column = 0)
    
    # Set up for scrollbar
    canvas = Canvas(frame)
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    canvas.create_window((0, 0), window = scrollable_frame, anchor ="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    ####
    
    all_e = []
    for i in range(len(s_list)):
        try:
            f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(s_list[i].office), "rb")
            e_list = pickle.load(f)
            f.close()
            all_e.append(e_list)        # all_e = list of e_list
        except:
            continue
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee_s", "wb")
    pickle.dump(all_e, f)               # Dump all_e to the new file
    f.close()
    frame_label1 = Label(scrollable_frame, text = "ID")
    frame_label1.grid(row = 0, column = 0)
    frame_label2 = Label(scrollable_frame, text = "Name")
    frame_label2.grid(row = 0, column = 1)
    frame_label3 = Label(scrollable_frame, text = "Gender")
    frame_label3.grid(row = 0, column = 2)
    frame_label4 = Label(scrollable_frame, text = "DoB")
    frame_label4.grid(row = 0, column = 3)
    frame_label5 = Label(scrollable_frame, text = "Office")
    frame_label5.grid(row = 0, column = 4)
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee_s", "rb") # Read the file
        all_e = pickle.load(f)
        f.close()
        for i in range(len(all_e)):
            for j in range(len(all_e[i])):
                frame_label1 = Label(scrollable_frame, text = "{}".format(all_e[i][j].id))
                frame_label1.grid(row = i * 10 + j + 1, column = 0)
                frame_label2 = Label(scrollable_frame, text = "{}".format(all_e[i][j].name))
                frame_label2.grid(row = i * 10 + j + 1, column = 1)
                frame_label3 = Label(scrollable_frame, text = "{}".format(all_e[i][j].gender))
                frame_label3.grid(row = i * 10 + j + 1, column = 2)
                frame_label4 = Label(scrollable_frame, text = "{}".format(all_e[i][j].DoB))
                frame_label4.grid(row = i * 10 + j + 1, column = 3)
                frame_label5 = Label(scrollable_frame, text = "{}".format(all_e[i][j].office))
                frame_label5.grid(row = i * 10 + j + 1, column = 4)
    except:
        messagebox.showwarning("", "No Employee Salary exist !", parent = window_m)     # Error dialog 


    frame2 = LabelFrame(temp, text = "EMPLOYEE SALARY")         # Create new frame
    frame2.grid(row = 0, column = 1)
    
    # Set up for scrollbar
    canvas2 = Canvas(frame2)
    scrollbar2 = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scrollable_frame2 = Frame(canvas2)

    scrollable_frame2.bind("<Configure>", lambda e: canvas2.configure(scrollregion = canvas2.bbox("all")))

    canvas2.create_window((0, 0), window = scrollable_frame2, anchor ="nw")
    canvas2.configure(yscrollcommand=scrollbar2.set)

    canvas2.pack(side="left", fill="both", expand=True)
    scrollbar2.pack(side="right", fill="y")
    ####

    all_p = []
    for i in range(len(s_list)):
        try:
            f = open("C:/Users/G40/Desktop/Human Resource/Database/Salary{}.pickle".format(s_list[i].office), "rb")
            p_list = pickle.load(f)
            f.close()
            all_p.append(p_list)        # all_p = list of p_list
        except:
            continue
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Salaries.pickle", "wb")
    pickle.dump(all_p, f)               # Dump all_p to the new file 
    f.close()
    frame_label1 = Label(scrollable_frame2, text = "ID")
    frame_label1.grid(row = 0, column = 0)
    frame_label2 = Label(scrollable_frame2, text = "Name")
    frame_label2.grid(row = 0, column = 1)
    frame_label3 = Label(scrollable_frame2, text = "Work Hour")
    frame_label3.grid(row = 0, column = 2)
    frame_label4 = Label(scrollable_frame2, text = "Wage/Hour")
    frame_label4.grid(row = 0, column = 3)
    frame_label5 = Label(scrollable_frame2, text = "Office")
    frame_label5.grid(row = 0, column = 4)
    frame_label6 = Label(scrollable_frame2, text = "Salary")
    frame_label6.grid(row = 0, column = 5)
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Salaries.pickle", "rb")  # Read the file
        all_p = pickle.load(f)
        f.close()
        for i in range(len(all_p)):
            for j in range(len(all_p[i])):
                frame_label1 = Label(scrollable_frame2, text = "{}".format(all_p[i][j].id))
                frame_label1.grid(row = i * 10 + j + 1, column = 0)
                frame_label2 = Label(scrollable_frame2, text = "{}".format(all_p[i][j].name))
                frame_label2.grid(row = i * 10 + j + 1, column = 1)
                frame_label3 = Label(scrollable_frame2, text = "{}h".format(all_p[i][j].working_hour))
                frame_label3.grid(row = i * 10 + j + 1, column = 2)
                frame_label4 = Label(scrollable_frame2, text = "{}$".format(all_p[i][j].wage))
                frame_label4.grid(row = i * 10 + j + 1, column = 3)
                frame_label5 = Label(scrollable_frame2, text = "{}".format(all_p[i][j].office))
                frame_label5.grid(row = i * 10 + j + 1, column = 4)
                frame_label6 = Label(scrollable_frame2, text = "{}$".format(all_p[i][j].total))
                frame_label6.grid(row = i * 10 + j + 1, column = 5)
    except:
        messagebox.showwarning("", "No Employee Salary exist !", parent = window_m)     # Error dialog 


def update_manager_info(manager_label, window_m):       # Update manager info
    temp = Toplevel()                                   # Create new toplevel on existed toplevel
    temp.title("MANAGER INFO")
    temp.grid_rowconfigure(0, weight=1)
    temp.grid_columnconfigure(0, weight=1)              # Set up grid()

    width = 400
    height = 400
    screen_width = temp.winfo_screenwidth()             # Get your screen width
    screen_height = temp.winfo_screenheight()           # Get your screen height

    x = (screen_width / 2) - (width / 2)
    y = (screen_height /2) - (height / 2)
    temp.geometry(f'{width}x{height}+{int(x)}+{int(y)}')      # Pop up window at the center of the screen

    temp.minsize(400, 400)
    temp.resizable(0, 0)                                # Prevent toplevel to expand

    def update(name, gender, DoB, password, window_m, manager_label, temp):
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Manager.pickle", "rb")          # Read file
        manager = pickle.load(f)
        f.close()
        if check_gender(gender.get()) == False:
            messagebox.showerror("", "Gender input Male or Female only !", parent = temp)      # Error dialog 
        else:
            try:
                birthday = DoB.get()
                birthday = birthday.split("/" , 2)
                x = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
                birthday = (datetime.date.strftime(x, "%d/%m/%Y"))
                id = manager.id
                manager = Manager(id, name.get(), gender.get(), birthday, password.get())
                f = open("C:/Users/G40/Desktop/Human Resource/Database/Manager.pickle", "wb")
                pickle.dump(manager, f)     # Dump Manager to new file
                f.close()
                manager_label.destroy()
                manager_label = Label(window_m, text = """

Your Information
---------------------------------
ID : {id}
Full Name : {name}
Gender : {gender}
DoB : {DoB}
Password : {password}
""".format(id = manager.id, name = manager.name, gender = manager.gender, DoB = manager.DoB, password = manager.password))
                manager_label.grid(row = 0, column = 1, sticky = W)
            except:
                messagebox.showerror("", "DoB must be in form (DD/MM/YYYY) !", parent = temp)       # Error dialog
            

    icon3 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
    label = Label(temp, image = icon3)
    label.grid(row = 0, column = 1)     # Display image 

    name = Entry(temp, width = 30)      # Input field for Full Name
    name.grid(row = 3, column = 1)
    label = Label(temp, text = "Full Name :")
    label.grid(row = 3, column = 0)

    gender = Entry(temp, width = 30)    # Input field for gender
    gender.grid(row = 4, column = 1)
    label = Label(temp, text = "Male/Female :")
    label.grid(row = 4, column =0)

    DoB = Entry(temp, width = 30)       # Input field for DoB
    DoB.grid(row = 5, column = 1)
    label = Label(temp, text = "DD/MM/YYYY :")
    label.grid(row = 5, column = 0)

    password = Entry(temp, width = 30)  # Input field for password
    password.grid(row = 6, column = 1)
    label = Label(temp, text = "Password :")
    label.grid(row = 6, column = 0)

    update_button = Button(temp, text = "Update Info", padx = 20, pady = 40, command = lambda: update(name, gender, DoB, password, window_m, manager_label, temp))
    update_button.grid(row = 3, column = 2, rowspan = 4)                        # Bind 'Update Info' button to update()

    label = Label(temp, text = "")
    label.grid(row = 8, column = 1)
    quit_button = Button(temp, text = "Exit Program", command = temp.destroy)   # Bind 'Exit Program' button to destroy()
    quit_button.grid(row = 9, column = 1)
    label = Label(temp, text = "")
    label.grid(row = 10, column = 1)

    temp.mainloop()     # Run GUI for toplevel

def main():
    window_m = Toplevel()       # Create new toplevel
    window_m.title("MANAGER")
    window_m.resizable(0, 0)    # Prevent toplevel to expand

    icon1 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))     
    label = Label(window_m, image = icon1)
    label.grid(row = 0, column = 0)     # Display image
    
    icon2 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
    label = Label(window_m, image = icon2)
    label.grid(row = 0, column = 2)     # Display image
    
    icon3 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/Manager.png"))
    label = Label(window_m, image = icon3)
    label.grid(row = 0, column = 4)     # Display image

    label = Label(window_m, text = "Staff Info")
    label.grid(row = 1, column = 1)

    label = Label(window_m, text = "      ")    # Add blank line
    label.grid(row = 0, column = 3)
    frame = LabelFrame(window_m, text = "STAFF INFO")       # Create new frame
    frame.grid(row = 1, column = 4, rowspan = 10, sticky = NE)
    frame2 = LabelFrame(window_m, text = "STAFF SALARY")    # Create new frame
    frame2.grid(row = 12, column = 4, rowspan = 10, sticky = NE)

    label = Label(window_m, text = "      ")    # Add blank line
    label.grid(row = 10, column = 3)
    label = Label(window_m, text = "      ")    # Add blank line
    label.grid(row = 11, column = 3)
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Manager.pickle", "rb")       # Read file
    manager = pickle.load(f)        
    f.close()

    manager_label = Label(window_m, text = """

Your Information
---------------------------------
ID : {id}
Full Name : {name}
Gender : {gender}
DoB : {DoB}
Password : {password}
""".format(id = manager.id, name = manager.name, gender = manager.gender, DoB = manager.DoB, password = manager.password))
    manager_label.grid(row = 0, column = 1, sticky = W)

    update_button = Button(window_m, text = "Update Info", pady = 44, command = lambda: update_manager_info(manager_label, window_m))
    update_button.grid(row = 0, column = 1, sticky = E)     # Bind 'Update Info' to update_manager_info() function

    id = Entry(window_m, width = 40)        # Input field for ID
    id.grid(row = 2, column = 1)
    label = Label(window_m, text = "ID :")
    label.grid(row = 2, column = 0)

    name = Entry(window_m, width = 40)      # Input field for Full Name
    name.grid(row = 3, column = 1)
    label = Label(window_m, text = "Full Name :")
    label.grid(row = 3, column = 0)

    gender = Entry(window_m, width = 40)    # Input field for gender
    gender.grid(row = 4, column = 1)
    label = Label(window_m, text = "Male/Female :")
    label.grid(row = 4, column =0)

    DoB = Entry(window_m, width = 40)       # Input field for DoB
    DoB.grid(row = 5, column = 1)
    label = Label(window_m, text = "DD/MM/YYYY :")
    label.grid(row = 5, column = 0)

    password = Entry(window_m, width = 40)  # Input field for password
    password.grid(row = 6, column = 1)
    label = Label(window_m, text = "Password :")
    label.grid(row = 6, column = 0)

    label = Label(window_m, text = "Choose Staff ID to delete")
    label.grid(row = 7, column = 2)
    del_id = Entry(window_m, width = 20)    # Input field for del_id
    del_id.grid(row = 6, column = 2)

    label = Label(window_m, text = "Choose Staff ID to update")
    label.grid(row = 18, column = 2)
    del_id2 = Entry(window_m, width = 22)       # Input field for del_id2
    del_id2.grid(row = 17, column = 2)
    label = Label(window_m, text = "      ")    # Add blank line
    label.grid(row = 19, column = 3)
    label = Label(window_m, text = "      ")    # Add blank line
    label.grid(row = 20, column = 3)
    

    label = Label(window_m, text = "Staff Salary")
    label.grid(row = 12, column = 1)

    working_hour = Entry(window_m, width = 40)  # Input field for Work Hour
    working_hour.grid(row = 13, column = 1)
    label = Label(window_m, text = "Work Hour :")
    label.grid(row = 13, column = 0)

    wage = Entry(window_m, width = 40)          # Input field for Wage/Hour
    wage.grid(row = 14, column = 1)
    label = Label(window_m, text = "Wage/Hour :")
    label.grid(row = 14, column = 0)

    add_button = Button(window_m, text = "Add Info", padx = 36, pady = 10, command = lambda: add_staff(id, name, gender, DoB, password, frame, window_m))
    add_button.grid(row = 2, column = 2, rowspan = 2)           # Bind 'Add Info' button to add_staff() function

    del_button = Button(window_m, text = "Del Info", padx = 38, pady = 10, command = lambda: del_staff(del_id, frame, window_m))
    del_button.grid(row = 4, column = 2, rowspan = 2)           # Bind 'Del Info' button to del_staff() function

    update_all_button = Button(window_m, text = "Update All", padx = 38, pady = 10, command = lambda: update_all_staff_salary(working_hour, wage, frame2, window_m))
    update_all_button.grid(row = 13, column = 2, rowspan = 2)   # Bind 'Update All' button to update_all_staff_salary() function

    update_one_button = Button(window_m, text = "Update One", padx = 34, pady = 10, command = lambda: update_one_staff_salary(del_id2, working_hour, wage, frame2, window_m))
    update_one_button.grid(row = 15, column = 2, rowspan = 2)   # Bind 'Update One' button to update_one_staff_salary() function

    
    
    show_button = Button(window_m, text = "Show all Employee\nInfo - Salary", padx = 66, pady = 33, bg = "black")
    show_button.grid(row = 16, column = 1, rowspan = 4)         # Black background for button
    show_button = Button(window_m, text = "Show all Employee\nInfo - Salary", padx = 44, pady = 22, command = lambda: show_all(window_m))
    show_button.grid(row = 16, column = 1, rowspan = 4)         # Bind 'Show all Employee Info - Salary' button to show_all() function
    
    show_staff(frame, window_m)
    show_all_staff_salary(frame2, window_m)
    
    window_m.mainloop()   

