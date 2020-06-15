from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk


root = Tk()
root.title("Vehicle Inventory System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
VEHICLE_NAME = StringVar()
VEHICLE_MODEL = StringVar()
VEHICLE_YEAR = IntVar()
VEHICLE_PRICE = IntVar()
VEHICLE_QTY = IntVar()
VEHICLE_COLOR = StringVar()
VEHICLE_MILEAGE = IntVar()
SEARCH = StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("Vee.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `vehicle` (vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, vehicle_name TEXT, vehicle_model TEXT, vehicle_year TEXT, vehicle_color TEXT, vehicle_mileage TEXT,  vehicle_qty TEXT, vehicle_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Vehicle Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Vehicle Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Vehicle Inventory System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)


def Home():
    global Home
    Home = Tk()
    Home.title("Vehicle Inventory System/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Vehicle Inventory System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#6666ff")


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Vehicle Inventory System/Add new")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()



def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Vehicle", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, height=600, width=700)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_vehiclename = Label(MidAddNew, text="Vehicle Name:", font=('arial', 15), bd=10)
    lbl_vehiclename.grid(row=0, sticky=W)
    lbl_vehiclemodel = Label(MidAddNew, text="Vehicle Model:", font=('arial', 15), bd=10)
    lbl_vehiclemodel.grid(row=1, sticky=W)
    lbl_vehicleyear = Label(MidAddNew, text="Vehicle Year:", font=('arial', 15), bd=10)
    lbl_vehicleyear.grid(row=2, sticky=W)
    lbl_color = Label(MidAddNew, text="Vehicle Color:", font=('arial', 15), bd=10)
    lbl_color.grid(row=3, sticky=W)
    lbl_vehiclemileage = Label(MidAddNew, text="Vehicle Mileage:", font=('arial', 15), bd=10)
    lbl_vehiclemileage.grid(row=4, sticky=W)
    lbl_qty = Label(MidAddNew, text="Vehicle Quantity:", font=('arial', 15), bd=10)
    lbl_qty.grid(row=5, sticky=W)
    lbl_price = Label(MidAddNew, text="Vehicle Price:", font=('arial', 15), bd=10)
    lbl_price.grid(row=6, sticky=W)

    vehiclename = Entry(MidAddNew, textvariable=VEHICLE_NAME, font=('arial', 25), width=15)
    vehiclename.grid(row=0, column=1)
    vehiclemodel = Entry(MidAddNew, textvariable=VEHICLE_MODEL, font=('arial', 25), width=15)
    vehiclemodel.grid(row=1, column=1)
    vehicleyear = Entry(MidAddNew, textvariable=VEHICLE_YEAR, font=('arial', 25), width=15)
    vehicleyear.grid(row=2, column=1)
    vehiclecolor = Entry(MidAddNew, textvariable=VEHICLE_COLOR, font=('arial', 25), width=15)
    vehiclecolor.grid(row=3, column=1)
    vehiclemileage = Entry(MidAddNew, textvariable=VEHICLE_MILEAGE, font=('arial', 25), width=15)
    vehiclemileage.grid(row=4, column=1)
    vehicleqty = Entry(MidAddNew, textvariable=VEHICLE_QTY, font=('arial', 25), width=15)
    vehicleqty.grid(row=5, column=1)
    vehicleprice = Entry(MidAddNew, textvariable=VEHICLE_PRICE, font=('arial', 25), width=15)
    vehicleprice.grid(row=6, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=15, bg="#009ACD", command=AddNew)
    btn_add.grid(row=7, columnspan=2, pady=20)


def AddNew():
    Database()
    cursor.execute("INSERT INTO `vehicle` (vehicle_name, vehicle_model, vehicle_year, vehicle_color, vehicle_mileage, vehicle_qty, vehicle_price) VALUES(?, ?, ?, ?, ?, ?, ?)",
                   (str(VEHICLE_NAME.get()), str(VEHICLE_MODEL.get()), int(VEHICLE_YEAR.get()), str(VEHICLE_COLOR.get()), int(VEHICLE_MILEAGE.get()),  int(VEHICLE_QTY.get()), int(VEHICLE_PRICE.get())))
    conn.commit()
    VEHICLE_NAME.set("")
    VEHICLE_MODEL.set("")
    VEHICLE_YEAR.set("")
    VEHICLE_COLOR.set("")
    VEHICLE_MILEAGE.set("")
    VEHICLE_PRICE.set("")
    VEHICLE_QTY.set("")
    cursor.close()
    conn.close()


def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Vehicles", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("VehicleID", "Vehicle Name", "Vehicle Model", "Vehicle Year", "Vehicle Color", "Vehicle Mileage", "Vehicle Qty", "Vehicle Price"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('VehicleID', text="VehicleID", anchor=W)
    tree.heading('Vehicle Name', text="Vehicle Name", anchor=W)
    tree.heading('Vehicle Model', text="Vehicle Model", anchor=W)
    tree.heading('Vehicle Year', text="Vehicle Year", anchor=W)
    tree.heading('Vehicle Color', text="Vehicle Color", anchor=W)
    tree.heading('Vehicle Mileage', text="Vehicle Mileage", anchor=W)
    tree.heading('Vehicle Qty', text="Vehicle Qty", anchor=W)
    tree.heading('Vehicle Price', text="Vehicle Price", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `vehicle`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `vehicle` WHERE `vehicle_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('',  'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")


def Delete():
    if not tree.selection():
        result = tkMessageBox.showerror('Vehicle Inventory System', 'You did not select a vehicle to delete', icon="warning")
    else:
        result = tkMessageBox.askquestion('Vehicle Inventory System', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `vehicle` WHERE `vehicle_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Vehicle Inventory System/View Vehicle")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()


def Logout():
    result = tkMessageBox.askquestion('Vehicle Inventory System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Account", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Vehicle Inventory System", font=('arial', 45))
lbl_display.pack()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
