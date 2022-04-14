from tkinter import *
from PIL import ImageTk, Image
import os
#hexidecimal for the blue = #156299
#hexidecimal for the red = #DA262E
#hexidecimal for the yellow = #FAE316

def help_page():
    global help_screen
    help_screen = Toplevel(main_screen)
    help_screen.title("Help")
    help_screen.geometry("700x500")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\db2.webp"))
    label = Label(help_screen, image = logo)
    label.photo = logo
    label.pack()
    Label(help_screen, text = "Help Page", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text = "Welcome to the help page, please select the issue \nyou are having from the drop down menu below:",  
    bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("700x500")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\db2.webp"))
    label = Label(login_screen, image = logo)
    label.photo = logo
    label.pack()
    Label(login_screen, text="Please enter credentials below to login", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ", fg = "#156299", font=("Sitka", 20)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password: ", fg = "#156299", font=("Sitka", 20)).pack()
    Label(login_screen, text="").pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg='#156299')
    main_screen.geometry("700x500")
    logo = ImageTk.PhotoImage(Image.open(r"C:\Users\bushj\Downloads\db2.webp"))
    label = Label(image = logo, width = "1000")
    label.pack()
    main_screen.title("Dutch Bros Product Analysis System")
    Label(text="Welcome to Dutch Bros Product Analysis System", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = login).pack()
    Label(text="").pack()
    Button(text="Help", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = help_page).pack()
 
    main_screen.mainloop()

main_account_screen()
   

 

 
   
 
 

 
 
