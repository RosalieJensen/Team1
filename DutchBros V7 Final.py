#importing all necessary python extensions
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import random
#hexidecimal for the blue = #156299
#hexidecimal for the red = #DA262E
#hexidecimal for the yellow = #FAE316

"""
Welcome to the Dutch Bros Product Analysis System
Creators: Dominic Deano, Rosalie Jensen, Kennedy Wallace, John Bush
"""

#INSTRUCTIONS
#STEP 1: Downlaod Dutch Bros Folder and save to your computer
#Step 2: Open dutchbros.jpg file from folder in VScode
#Step 3: Right click on dutchbros.jpg tab header and select Copy Path
#Step 4: Paste path into photo variable after photo =
    #Example: photo = r"C:\Users\bushj\Downloads\coffee.jpg"
    #Don't forget the r before the Copy Path and to put the copy path in ""
#Step 5: Application is ready to run!

global photo
photo = r"C:\Users\bushj\OneDrive\Desktop\Dutch Bros\dutchbros.jpg"


#help page method has drop down and user entry
def help_page():
    global help_screen
    help_screen = Toplevel(main_screen)
    help_screen.title("Help")
    help_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(photo))
    label = Label(help_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    Label(help_screen, text = "Help Page", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text = "Welcome to the help page, please select the issue \nyou are having from the drop down menu below:",  
    bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text="").pack()

    #help page dropdown menu
    firstOption = StringVar()
    firstOption.set("Login screen not working") 
    w = OptionMenu(help_screen, firstOption, "Login screen not working", "Analysis system malfunctioning", "Application crashes unexpectedly", "Statistics not working", "Application is too slow")
    w.configure(width = 25)
    w.configure(height = 1)
    w.configure(font=("Sitka", 15))
    w.configure(fg='#156299')
    w.pack()

    #help page issue entry
    issue = StringVar()
    Label(help_screen, text="").pack()
    Label(help_screen, text = "If your issue is not listed above, please type your issue below:",  
    bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(help_screen, text="").pack()
    issuebox = Entry(help_screen, textvariable=issue, width = "70")
    issuebox.pack()

    #Button to submit feedback
    Button(help_screen, text="Submit", width=10, height=10, fg = "#156299", font=("Sitka", 20), bg = "#FAE316").pack()
    help_screen.configure(bg='#156299')


#login page method
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(photo))
    label = Label(login_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()

    #defining variables for login activities
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    #Labels and entries for username and password
    Label(login_screen, text="Please enter credentials below to login", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ", fg = "#156299", font=("Sitka", 20), width="12", height="2").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify,width="28")
    username_login_entry.pack()
    Label(login_screen, text="Password: ", fg = "#156299", font=("Sitka", 20),width="12", height="2").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,width="28")
    password_login_entry.pack()

    #Login Button
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=20, height=20, fg = "#156299", font=("Sitka", 20), bg = "#FAE316", command = login_verify).pack()
    Button(login_screen, text="Help", height="2", width="8", fg = "#DA262E", bg="#FAE316", font=("Sitka", 15), command = help_page).place(x = 75, y = 625)
    login_screen.configure(bg='#156299')

#login_verify() is the function for the logic of logging the user in
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    adminUserName = str("admin")
    adminPassword = str("dbros")
    #lets user in if credentials are correct
    if username1 == adminUserName and password1 == adminPassword:
        login_sucess()
    #displays error message if credentials are invalid
    else:
        password_not_recognised()


#Brings up page to enter system when user correctly enters credentials
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(photo))
    label = Label(login_success_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    Label(login_success_screen, text="Success", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Click Here to Enter the System", 
    width=25, height=7, fg = "#DA262E", font=("Sitka", 15), bg = "#FAE316", command = product_analysis).pack()
    login_success_screen.configure(bg='#156299')

#Error message for invalid credentials
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("400x100")
    Label(password_not_recog_screen, text="Invalid Username or Password", fg = "#156299", font=("Sitka", 20)).pack()

#product_analysis() is the main method for the page and holds all the calculations   
def product_analysis():
    global analysis_screen
    analysis_screen = Toplevel(login_success_screen)
    analysis_screen.title("Product Analysis")
    analysis_screen.geometry("1200x900")
    logo = ImageTk.PhotoImage(Image.open(photo))
    label = Label(analysis_screen, image = logo, width= "900")
    label.photo = logo
    label.pack()
    analysis_screen.configure(bg = "#156299")
    Label(analysis_screen, text="Product Analysis System", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    
    #treeview style
    style = ttk.Style()
    style.theme_use('clam')

    #treeview creates the table on the product analysis screen
    columns = ('PO#', 'Order Price', '# of Items')
    tree = ttk.Treeview(analysis_screen, column=columns, show='headings', height = 20)
    tree.heading('PO#', text='PO#')
    tree.heading('Order Price', text='Order Price')
    tree.heading('# of Items', text='# of Items')

    #random item and price numbers used to populate treeview
    pricelist = ["1","2","3","4","5","6","7","8","9", "10", "11", "12", "13", "14", "15", "17", "20", "22", "25", "30"]
    itemlist  = ["0","1","2","3","4","5","6","7","8","9", "10"]

    #treelist created to create list of random values for PO#, Order Price, and # of Items to populate treeview with
    treelist = []
    for n in range(1, 100):
        treelist.append((f'{n}', f'{random.choice(pricelist)}', f'{random.choice(itemlist)}'))

    #for loop adds treelist values to the treeview
    for randomvalue in treelist:
        tree.insert('', END, values=randomvalue)

    tree.pack(side = LEFT)

    Label(analysis_screen, text= "Statistics", bg="#FAE316", width="40", height="2", fg = "#DA262E", font=("Sitka", 20)).place(x=600, y=412)

    #global calculation variables to use in other methods
    global totalOrders
    global totalSales
    global totalItems
    global floatAveragePriceDeciaml
    global floatAverageItemsDeciaml
    
    #calculations
    totalOrders = len(treelist)
    totalSales = sum(float(tree.set(item,1)) for item in tree.get_children())
    totalItems = sum(float(tree.set(item,2)) for item in tree.get_children())

    averagePrice = (totalSales/totalOrders)
    averageItems = (totalItems/totalOrders)

    #calculations
    averagePriceDecimal = "{:.2f}".format(averagePrice)
    averageItemsDecimal = "{:.2f}".format(averageItems)
    floatAveragePriceDeciaml = float(averagePriceDecimal)
    floatAverageItemsDeciaml = float(averageItemsDecimal)
    
    #m1 and m2 are for first selections and are used later to reference selected drop down option
    global m1
    global m2
    m1 = StringVar()
    m2 = StringVar()
    m1.set("Total Orders")
    m2.set("Total Orders")
   
    #first optionmenu for statistics
    menu1 = OptionMenu(analysis_screen, m1, "Total Orders", "Total Sales", "Total Items Purchased", "Average Order Price", "Average # of Items")
    menu1.configure(width = 25)
    menu1.configure(height = 1)
    menu1.configure(font=("Sitka", 15))
    menu1.configure(fg='#156299')
    menu1.place(x=625, y=575)

    #second optionmenu for statistics
    menu2 = OptionMenu(analysis_screen, m2, "Total Orders", "Total Sales", "Total Items Purchased", "Average Order Price", "Average # of Items")
    menu2.configure(width = 25)
    menu2.configure(height = 1)
    menu2.configure(font=("Sitka", 15))
    menu2.configure(fg='#156299')
    menu2.place(x=625, y=700)
 
    #calculation and help buttons
    Button(analysis_screen, text= "Calculate", width=15, height=2, fg = "#156299", font=("Sitka", 20), bg = "#FAE316", command= calculation).place(x=800, y=790)
    Button(analysis_screen, text="Help", height="2", width="8", fg = "#DA262E", bg="#FAE316", font=("Sitka", 15), command = help_page).place(x = 650, y =800)

 #calculation method allows both calculations to be referenced by single command
def calculation():
    calculation1()
    calculation2()

#takes the selected option from first optionmenu and puts label on the screen with the matching calculation
def calculation1():
    calclist = ["Total Orders", "Total Sales", "Total Items Purchased", "Average Order Price", "Average # of Items"]
    calc1 = m1.get()
    calcValue = float()
    if calc1 == calclist[0]:
        calcValue = totalOrders
    elif calc1 == calclist[1]:
        calcValue = totalSales
    elif calc1 == calclist[2]:
        calcValue = totalItems
    elif calc1 == calclist[3]:
        calcValue = floatAveragePriceDeciaml
    else:
        calcValue = floatAverageItemsDeciaml

    Label(analysis_screen, text = str(calcValue), bg="#FAE316", width="10", height="2", fg = "#DA262E", font=("Sitka", 20)).place(x= 1000, y= 565)

#takes the selected option from second optionmenu and puts label on the screen with the matching calculation
def calculation2():
    calclist = ["Total Orders", "Total Sales", "Total Items Purchased", "Average Order Price", "Average # of Items"]
    calc2 = m2.get()
    calcValue = float()
    if calc2 == calclist[0]:
        calcValue = totalOrders
    elif calc2 == calclist[1]:
        calcValue = totalSales
    elif calc2 == calclist[2]:
        calcValue = totalItems
    elif calc2 == calclist[3]:
        calcValue = floatAveragePriceDeciaml
    else:
        calcValue = floatAverageItemsDeciaml

    Label(analysis_screen, text = str(calcValue), bg="#FAE316", width="10", height="2", fg = "#DA262E", font=("Sitka", 20)).place(x=1000, y= 685)
         

#main method creates instance of TK and is the first screen the user sees when they login
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg='#156299')
    main_screen.geometry("900x700")
    logo = ImageTk.PhotoImage(Image.open(photo))
    label = Label(image = logo, width = "900")
    label.pack()
    main_screen.title("Dutch Bros Product Analysis System")
    Label(text="Welcome to Dutch Bros Product Analysis System", bg="#FAE316", width="300", height="2", fg = "#DA262E", font=("Sitka", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = login).pack()
    Label(text="").pack()
    Button(text="Help", height="2", width="30",fg = "#156299", font=("Sitka", 20), command = help_page).pack()
 
    main_screen.mainloop()

#main method to run program
main_account_screen()