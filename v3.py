from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import random
#hexidecimal for the blue = #156299
#hexidecimal for the red = #DA262E
#hexidecimal for the yellow = #FAE316

def help_page():
    global help_screen
    help_screen = Toplevel(main_screen)
    help_screen.title("Help")
    help_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\coffee.jpg"))
    label = Label(help_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    Label(help_screen, text = "Help Page", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text = "Welcome to the help page, please select the issue \nyou are having from the drop down menu below:",  
    bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text="").pack()

    firstOption = StringVar()
    firstOption.set("Login screen not working")
    w = OptionMenu(help_screen, firstOption, "Login screen not working", "Analysis system malfunctioning", "Application crashes unexpectedly", "Statistics not working", "Application is too slow")
    w.configure(width = 25)
    w.configure(height = 1)
    w.configure(font=("Sitka", 15))
    w.configure(fg='#156299')
    w.pack()

    issue = StringVar()
    Label(help_screen, text="").pack()
    Label(help_screen, text = "If your issue is not listed above, please type your issue below:",  
    bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text="").pack()
    issuebox = Entry(help_screen, textvariable=issue, width = "70")
    issuebox.pack()

    Button(help_screen, text="Submit", width=10, height=10, fg = "#156299", font=("Sitka", 20), bg = "#FAE316").pack()
    help_screen.configure(bg='#156299')

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\coffee.jpg"))
    label = Label(login_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()

    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 

    Label(login_screen, text="Please enter credentials below to login", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ", fg = "#156299", font=("Sitka", 20), width="12", height="2").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify,width="28")
    username_login_entry.pack()
    Label(login_screen, text="Password: ", fg = "#156299", font=("Sitka", 20),width="12", height="2").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,width="28")
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=20, height=20, fg = "#156299", font=("Sitka", 20), bg = "#FAE316", command = login_verify).pack()

    login_screen.configure(bg='#156299')

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    adminUserName = str("admin")
    adminPassword = str("dbros")
    if username1 == adminUserName and password1 == adminPassword:
        login_sucess()
 
    else:
        password_not_recognised()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\coffee.jpg"))
    label = Label(login_success_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    Label(login_success_screen, text="Success", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Click Here to Enter the System",
    width=25, height=7, fg = "#DA262E", font=("Sitka", 15), bg = "#FAE316", command = product_analysis).pack()
    login_success_screen.configure(bg='#156299')

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("400x100")
    Label(password_not_recog_screen, text="Invalid Username or Password", fg = "#156299", font=("Sitka", 20)).pack()
   
def product_analysis():
    global analysis_screen
    analysis_screen = Toplevel(login_success_screen)
    analysis_screen.title("Product Analysis")
    analysis_screen.geometry("1200x900")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\coffee.jpg"))
    label = Label(analysis_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    analysis_screen.configure(bg = "#156299")
    Label(analysis_screen, text="Product Analysis System", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
   
    style = ttk.Style()
    style.theme_use('clam')

    columns = ('PO#', 'Order Price', '# of Items')
    tree = ttk.Treeview(analysis_screen, column=columns, show='headings', height = 20)
    tree.heading('PO#', text='PO#')
    tree.heading('Order Price', text='Order Price')
    tree.heading('# of Items', text='# of Items')

    pricelist = ["1","2","3","4","5","6","7","8","9", "10", "11", "12", "13", "14", "15", "17", "20", "22", "25", "30"]
    itemlist  = ["0","1","2","3","4","5","6","7","8","9", "10"]

    treelist = []
    for n in range(1, 100):
        treelist.append((f'{n}', f'{random.choice(pricelist)}', f'{random.choice(itemlist)}'))


    for randomvalue in treelist:
        tree.insert('', END, values=randomvalue)

    tree.pack(side = LEFT)

    Label(analysis_screen, text="Statistics", bg="#FAE316", width="40", height="2", fg = "#DA262E", font=("Sitka", 20)).place(x=600, y=412)

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg='#156299')
    main_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\coffee.jpg"))
    label = Label(image = logo, width = "900")
    label.pack()
    main_screen.title("Dutch Bros Product Analysis System")
    Label(text="Welcome to Dutch Bros Product Analysis System", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = login).pack()
    Label(text="").pack()
    Button(text="Help", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = help_page).pack()
 
    main_screen.mainloop()

main_account_screen()