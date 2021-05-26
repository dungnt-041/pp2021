import pickle
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import math
import datetime
from Domains.Staff import Staff                 # Import class Staff
from Domains.Employee import Employee           # Import class Employee
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

def add_employee(id, name, gender, DoB, office, frame, window_s):       # Add employee info to e_list
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "rb")     # Read Employee{office}.pickle
        e_list = pickle.load(f)
        f.close()
    except:
        e_list =[]      # Create new list if no data
    if prevent_duplicate(id.get(), e_list) == False:
        messagebox.showerror("", "ID already existed !", parent = window_s)     # Show error dialog
    else:
        if check_gender(gender.get()) == False:
            messagebox.showerror("", "Gender input Male or Female only !", parent = window_s)       # Show error dialog
        else:
            try:
                birthday = DoB.get()
                birthday = birthday.split("/" , 2)
                x = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
                birthday = (datetime.date.strftime(x, "%d/%m/%Y"))      # Show DoB in form DD/MM/YYYY
                e_list.append(Employee(id.get(), name.get(), gender.get(), birthday, office))
                e_list = sorted(e_list, key = lambda x: x.id)       # Sort list base on ID
                id.delete(0, END)
                name.delete(0, END)
                gender.delete(0, END)
                DoB.delete(0, END)      # Clear input fields
            except:
                messagebox.showerror("", "DoB must be in form (DD/MM/YYYY) !", parent = window_s)       # Show error dialog
            if len(e_list) > 10 :
                messagebox.showwarning("", "No more than 10 Employee !", parent = window_s)     # Show error dialog
            else:
                f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "wb")
                pickle.dump(e_list, f)      # Dump e_list to new file
                f.close()
                show_employee(office, frame, window_s)                # Show e_list

def del_employee(del_id, office, frame, window_s):
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "rb")     # Read file
    e_list = pickle.load(f)
    f.close()
    if not any(staff.id == del_id.get() for staff in e_list):
        messagebox.showerror("", "ID Not Found !", parent = window_s)       # Show error dialog
    else:
        for i in range(len(e_list)):
            if e_list[i - 1].id == del_id.get():
                e_list.pop(i - 1)
        e_list = sorted(e_list, key = lambda x: x.id)       # Sort list base on ID
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "wb")
        pickle.dump(e_list, f)      # Dump e_list to new file
        f.close()
        del_id.delete(0, END)
        show_employee(office, frame)                # Show e_list
    
def show_employee(office, frame, window_s):                # Show e_list
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
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "rb")     # Read file
        e_list = pickle.load(f)
        f.close()
        for i in range(len(e_list)):
            frame_label1 = Label(frame, text = "{}".format(e_list[i].id))
            frame_label1.grid(row = i + 1, column = 0)
            frame_label2 = Label(frame, text = "{}".format(e_list[i].name))
            frame_label2.grid(row = i + 1, column = 1)
            frame_label3 = Label(frame, text = "{}".format(e_list[i].gender))
            frame_label3.grid(row = i + 1, column = 2)
            frame_label4 = Label(frame, text = "{}".format(e_list[i].DoB))
            frame_label4.grid(row = i + 1, column = 3)
            frame_label5 = Label(frame, text = "{}".format(e_list[i].office))
            frame_label5.grid(row = i + 1, column = 4)
    except:
        messagebox.showwarning("", "No Employee Info exist.\nPlease add Employee Info !", parent = window_s)        # Show error dialog        

def update_all_employee_salary(working_hour, wage, office, frame, window_s):
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "rb")     # Read file
    e_list = pickle.load(f)
    f.close()
    p_list = [] 
    try: 
        if float(working_hour.get()) > 200.0:
            messagebox.showwarning("", "Work Hour : No more than 200h", parent = window_s)      # Show error dialog
        else:
            working_hour2 = float(working_hour.get())       # String to float
            try: 
                if float(wage.get()) > 9999.0:
                    messagebox.showwarning("", "Wage : No more than 9999$ !", parent = window_s)        # Show error dialog
                else:
                    for i in range(len(e_list)):
                        wage2 = float(wage.get())       # String to float
                        total = wage2 * working_hour2
                        total = math.floor(total)
                        id = e_list[i].id
                        name = e_list[i].name
                        office = id[0]
                        p_list.append(Salary(id, name, office, working_hour2, wage2, total))
                    p_list = sorted(p_list, key = lambda x: x.id)       # Sort list base on ID
                    f = open("C:/Users/G40/Desktop/Human Resource/Database/Salary{}.pickle".format(office), "wb")
                    pickle.dump(p_list, f)      # Dump p_list to new file
                    f.close()
                    show_all_employee_salary(office, frame, window_s)                # Show p_list
            except:
                    messagebox.showwarning("", "Wage : Number only !", parent = window_s)       # Show error dialog 
    except:
        messagebox.showwarning("", "Work Hour : Number only !", parent = window_s)      # Show error dialog
                    
def show_all_employee_salary(office, frame, window_s):                # Show p_list
    for widget in frame.winfo_children():
        widget.destroy()                         # Reset frame
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
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Salary{}.pickle".format(office), "rb")       # Read file
        p_list = pickle.load(f)
        f.close()
        for i in range(len(p_list)):
            frame_label1 = Label(frame, text = "{}".format(p_list[i].id))
            frame_label1.grid(row = i + 1, column = 0)
            frame_label2 = Label(frame, text = "{}".format(p_list[i].name))
            frame_label2.grid(row = i + 1, column = 1)
            frame_label3 = Label(frame, text = "{}h".format(p_list[i].working_hour))
            frame_label3.grid(row = i + 1, column = 2)
            frame_label4 = Label(frame, text = "{}$".format(p_list[i].wage))
            frame_label4.grid(row = i + 1, column = 3)
            frame_label5 = Label(frame, text = "{}".format(p_list[i].office))
            frame_label5.grid(row = i + 1, column = 4)
            frame_label6 = Label(frame, text = "{}$".format(p_list[i].total))
            frame_label6.grid(row = i + 1, column = 5)
    except:
        messagebox.showwarning("", "No Staff Salary exist.\nPlease update Staff Salary !", parent = window_s)       # Show error dialog       

def update_one_employee_salary(id, working_hour, wage, office, frame, window_s):
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Salary{}.pickle".format(office), "rb")       # Read file
        p_list = pickle.load(f)
        f.close()
    except:
        p_list = []
    f = open("C:/Users/G40/Desktop/Human Resource/Database/Employee{}.pickle".format(office), "rb")     # Read file
    e_list = pickle.load(f)
    f.close()
    if not any(employee.id == id.get() for employee in e_list):
        messagebox.showerror("", "ID Not Found !", parent = window_s)
    else:
        for i in range(len(p_list)):
            if p_list[i - 1].id == id.get():
                p_list.pop(i - 1)
        for i in range(len(e_list)):
            if e_list[i].id == id.get():
                name = e_list[i].name
                id2 = id.get()
        try: 
            if float(working_hour.get()) > 200.0:
                messagebox.showwarning("", "Work Hour : No more than 200h", parent = window_s)      # Show error dialog
            else:
                working_hour2 = float(working_hour.get())       # String to float
                try: 
                    if float(wage.get()) > 9999.0:
                        messagebox.showwarning("", "Wage : No more than 9999$ !", parent = window_s)    # Show error dialog        
                    else:
                        wage2 = float(wage.get())       # String to float
                        total = wage2 * working_hour2
                        total = math.floor(total)
                        p_list.append(Salary(id2, name, office, working_hour2, wage2, total))
                        p_list = sorted(p_list, key = lambda x: x.id)       # Sort list base on ID
                        f = open("C:/Users/G40/Desktop/Human Resource/Database/Salary{}.pickle".format(office), "wb")
                        pickle.dump(p_list, f)      # Dump p_list to new file
                        f.close()
                        show_all_employee_salary(office, frame, window_s)                # Show p_list
                except:
                        messagebox.showwarning("", "Wage : Number only ! ", parent = window_s)      # Show error dialog 
        except:
            messagebox.showwarning("", "Work Hour : Number only !", parent = window_s)      # Show error dialog

def update_staff_info(staff_lable, office, window_s):       # Update staff info
    temp = Toplevel()                                       # Create new toplevel on existed toplevel
    temp.title("STAFF INFO")
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

    def update(name, gender, DoB, password, office, window_s, staff_lable, temp):
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(office), "rb")        # Read file
        staff = pickle.load(f)
        f.close()
        if check_gender(gender.get()) == False:
            messagebox.showerror("", "Gender input Male or Female only !", parent = temp)       # Show error dialog
        else:
            try:
                birthday = DoB.get()
                birthday = birthday.split("/" , 2)
                x = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
                birthday = (datetime.date.strftime(x, "%d/%m/%Y"))
                id = staff.id
                staff = Staff(id, name.get(), gender.get(), birthday, office, password.get())
                f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(office), "wb")
                pickle.dump(staff, f)      # Dump staff to new file
                f.close()
                staff_lable.destroy()
                staff_lable = Label(window_s, text = """

Your Information
---------------------------------
ID : {id}
Full Name : {name}
Gender : {gender}
DoB : {DoB}
Office : {office}
Password : {password}
""".format(id = staff.id, name = staff.name, gender = staff.gender, DoB = staff.DoB, office = staff.office, password = staff.password))
                staff_lable.grid(row = 0, column = 1, sticky = W)
            except:
                messagebox.showerror("", "DoB must be in form (DD/MM/YYYY) !", parent = temp)       # Show error dialog
            

    icon3 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
    label = Label(temp, image = icon3)
    label.grid(row = 0, column = 1)     # Display image

    name = Entry(temp, width = 30)        # Input field for Full Name
    name.grid(row = 3, column = 1)
    label = Label(temp, text = "Full Name :")
    label.grid(row = 3, column = 0)

    gender = Entry(temp, width = 30)        # Input field for gender
    gender.grid(row = 4, column = 1)
    label = Label(temp, text = "Male/Female :")
    label.grid(row = 4, column =0)

    DoB = Entry(temp, width = 30)        # Input field for DoB
    DoB.grid(row = 5, column = 1)
    label = Label(temp, text = "DD/MM/YYYY :")
    label.grid(row = 5, column = 0)

    password = Entry(temp, width = 30)        # Input field for Password
    password.grid(row = 6, column = 1)
    label = Label(temp, text = "Password :")
    label.grid(row = 6, column = 0)

    update_button = Button(temp, text = "Update Info", padx = 20, pady = 40, command = lambda: update(name, gender, DoB, password, office, window_s, staff_lable, temp))
    update_button.grid(row = 3, column = 2, rowspan = 4)   # Bind 'Update Info' button to update() function

    label = Label(temp, text = "")    # Add blank line
    label.grid(row = 8, column = 1)
    quit_button = Button(temp, text = "Exit Program", command = temp.destroy)
    quit_button.grid(row = 9, column = 1)
    label = Label(temp, text = "")    # Add blank line
    label.grid(row = 10, column = 1)

    temp.mainloop() # run toplevel GUI

def main(office):
    window_s = Toplevel()       # Create new toplevel 
    window_s.title("STAFF")
    window_s.resizable(0, 0)

    icon1 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
    label = Label(window_s, image = icon1)
    label.grid(row = 0, column = 0)     # Display image
    
    icon2 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
    label = Label(window_s, image = icon2)
    label.grid(row = 0, column = 2)     # Display image
    
    icon3 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/Staff.png"))
    label = Label(window_s, image = icon3)
    label.grid(row = 0, column = 4)     # Display image

    label = Label(window_s, text = "Employee Info")
    label.grid(row = 1, column = 1)

    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 0, column = 3)
    frame = LabelFrame(window_s, text = "EMPLOYEE INFO")        # Create new frame
    frame.grid(row = 1, column = 4, rowspan = 12, sticky = N)
    frame2 = LabelFrame(window_s, text = "EMPLOYEE SALARY")        # Create new frame
    frame2.grid(row = 14, column = 4, rowspan = 12, sticky = NW)

    f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(office), "rb")        # Read file
    staff = pickle.load(f)
    f.close()

    staff_lable = Label(window_s, text = """

Your Information
---------------------------------
ID : {id}
Full Name : {name}
Gender : {gender}
DoB : {DoB}
Office : {office}
Password : {password}
""".format(id = staff.id, name = staff.name, gender = staff.gender, DoB = staff.DoB, office = staff.office, password = staff.password))
    staff_lable.grid(row = 0, column = 1, sticky = W)

    update_button = Button(window_s, text = "Update Info", pady = 44, command = lambda: update_staff_info(staff_lable, office, window_s))
    update_button.grid(row = 0, column = 1, sticky = E)   # Bind 'Update Info' button to update_staff_info() function

    id = Entry(window_s, width = 40)        # Input field for ID
    id.grid(row = 2, column = 1)
    label = Label(window_s, text = "ID :")        
    label.grid(row = 2, column = 0)

    name = Entry(window_s, width = 40)        # Input field for Full Name
    name.grid(row = 3, column = 1)
    label = Label(window_s, text = "Full Name :")
    label.grid(row = 3, column = 0)

    gender = Entry(window_s, width = 40)        # Input field for gender
    gender.grid(row = 4, column = 1)
    label = Label(window_s, text = "Male/Female :")
    label.grid(row = 4, column =0)

    DoB = Entry(window_s, width = 40)        # Input field forDoB
    DoB.grid(row = 5, column = 1)
    label = Label(window_s, text = "DD/MM/YYYY :")
    label.grid(row = 5, column = 0)

    label = Label(window_s, text = "Choose Employee ID to delete")
    label.grid(row = 7, column = 2)
    del_id = Entry(window_s, width = 20)        # Input field for del_id
    del_id.grid(row = 6, column = 2)

    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 8, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 9, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 10, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 11, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 12, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 13, column = 3)

    label = Label(window_s, text = "Employee Salary")
    label.grid(row = 14, column = 1)

    working_hour = Entry(window_s, width = 40)        # Input field for Work Hour
    working_hour.grid(row = 15, column = 1)
    label = Label(window_s, text = "Work Hour :")
    label.grid(row = 15, column = 0)

    wage = Entry(window_s, width = 40)        # Input field for Wage/Hour
    wage.grid(row = 16, column = 1)
    label = Label(window_s, text = "Wage/Hour :")
    label.grid(row = 16, column = 0)

    label = Label(window_s, text = "Choose Employee ID to update")
    label.grid(row = 20, column = 2)
    del_id2 = Entry(window_s, width = 22)        # Input field for del_id2
    del_id2.grid(row = 19, column = 2)

    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 21, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 22, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 23, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 24, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 25, column = 3)
    label = Label(window_s, text = "      ")    # Add blank line
    label.grid(row = 26, column = 3)

    add_button = Button(window_s, text = "Add Info", padx = 36, pady = 10, command = lambda: add_employee(id, name, gender, DoB, office, frame, window_s))
    add_button.grid(row = 2, column = 2, rowspan = 2)   # Bind 'Add Info' button to add_employee() function

    del_button = Button(window_s, text = "Del Info", padx = 38, pady = 10, command = lambda: del_employee(del_id, office, frame, window_s))
    del_button.grid(row = 4, column = 2, rowspan = 2)   # Bind 'Del Info' button to del_employee() function

    update_all_button = Button(window_s, text = "Update All", padx = 38, pady = 10, command = lambda: update_all_employee_salary(working_hour, wage, office, frame2, window_s))
    update_all_button.grid(row = 15, column = 2, rowspan = 2)   # Bind 'Update All' button to update_all_employee_salary() function

    update_one_button = Button(window_s, text = "Update One", padx = 34, pady = 10, command = lambda: update_one_employee_salary(del_id2, working_hour, wage, office, frame2, window_s))
    update_one_button.grid(row = 17, column = 2, rowspan = 2)   # Bind 'Update One' button to update_one_employee_salary() function

    show_employee(office, frame, window_s)
    show_all_employee_salary(office, frame2, window_s)
    
    window_s.mainloop()   

