import pickle
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import manager      # Import manager module      
import staff        # Impor staff module
window = Tk()
window.title("HUMAN RESOURCE MANAGEMENT")   # Set the window title

window.grid_rowconfigure(0, weight=1)       # Set up to display label in the center using grid()
window.grid_columnconfigure(0, weight=1)    

width = 440
height = 460
screen_width = window.winfo_screenwidth()   # Your screen width
screen_height = window.winfo_screenheight() # Your screen height

x = (screen_width / 2) - (width / 2)
y = (screen_height /2) - (height / 2)
window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')      # Pop up window at the center of the screen

icon = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher.png"))
label = Label(image = icon)
label.grid(row = 0)                                         # Display dreamcatcher.png (image)

label = Label(window, text = "")                            # Add a blank line in the GUI 
label.grid(row = 2)

icon2 = ImageTk.PhotoImage(Image.open("C:/Users/G40/Desktop/Human Resource/dreamcatcher2.png"))
label = Label(image = icon2)
label.grid(row = 3)                                         # Display dreamcatcher2.png (image)


window.minsize(400, 400)                                    # Minimum size of window when pop up
window.resizable(0, 0)                                      # Prevent window to expand





def login():
    office = check_user_account(username, password)        
    if office == "Alpha":
        manager.main()                      # If check_user_account() return A --> Manager                                         
    else:
        staff.main(office[0])                  # Else --> Staff 
    

def check_user_account(username, password):
    username = username.get()
    password = password.get()
    f1 =open("C:/Users/G40/Desktop/Human Resource/Database/Staff_s.pickle", "rb")    # Read Staffs.picke 
    temp = pickle.load(f1)
    f1.close()
    f2 =open("C:/Users/G40/Desktop/Human Resource/Database/Manager.pickle", "rb")   # Read Manager.pickle
    temp.append(pickle.load(f2))
    f2.close()
    
    if not any (obj.id == username for obj in temp):                    # temp = Staffs + Manager
        messagebox.showerror("", "Username Not Found !")                # Show error dialoge
    else:
        for i in range(len(temp)):
            if temp[i].id == username:                                  # Username = id
                check = temp[i].password                                
        
        if password != check:
            messagebox.showerror("", "Incorrect Password !")            # Show error dialog 
        else:
            office = username
    return office                                                           # Office = first letter of Username

username_label = Label(window, text = "Username")
username_label.grid(row = 4)
username = Entry(window, width = 40)                                        # Input field for Username
username.grid(row = 5)
password_label = Label(window, text = "Password")
password_label.grid(row = 6)
password = Entry(window, width = 40)                                        # Input field for Password
password.grid(row = 7)

label = Label(window, text = "")                                            # Add blank line
label.grid(row = 8)
login_button = Button(window, text = "LOGIN", command = login)              # Bind 'Login' button to login() function
login_button.grid(row = 9)

label = Label(window, text = "")                                            # Add blank line
label.grid(row = 10)
quit_button = Button(window, text = "Exit program", command = window.quit)  # Bind 'Exit program' button to quit()
quit_button.grid(row = 11)
label = Label(window, text = "")                                            # Add blank line
label.grid(row = 12)

window.mainloop()                                                           # Run GUI