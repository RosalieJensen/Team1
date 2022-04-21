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
