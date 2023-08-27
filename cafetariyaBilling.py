from tkinter import *
import pymysql
from tkinter import messagebox,filedialog
from tkinter import ttk
from datetime import datetime

taz=Tk()
width=taz.winfo_screenwidth()
#print(width)
height=taz.winfo_screenheight()
#print(height)

tazTV=ttk.Treeview(height=10,columns=(' Item Name '' Rate ',' Type '))
tazTV1=ttk.Treeview(height=10,columns=('Date ''Name','Rate','Type','Total'))

### for char input
def only_char_input(P):
    if P.isalpha() or P=='' or P.isspace():
        return True
    return False

callbackChar=taz.register(only_char_input)

## for digit
def only_numeric_input(P):
    if P.isdigit() or P=='':

        return True
    return False
callbackNum=taz.register(only_numeric_input)
#################       database connection
def dbconfig():
    global coon,mycursor
    coon=pymysql.connect(host="localhost",user="root",db="hmsystem")
    mycursor=coon.cursor()

##################  clear screen
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()



def mainheading():
    label=Label(taz,text="CAFETERIA BILLING SYSTEM",fg="red",bg="yellow",font=("Comic Sans Ms",40,"bold"),padx=300,pady=0)
    label.grid(row=0,columnspan=4)

usernameVar=StringVar()
passwordVar=StringVar()

################# Logout ########
def logout():
    clear_screen()
    mainheading()
    loginwindow()


#################### Login Window #########
def loginwindow():
    usernameVar.set("")
    passwordVar.set("")

    labellogin=Label(taz,text="Admin Login",font=("Ariel",25,"bold"))
    labellogin.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    usernamelabel=Label(taz,text="User Name",font=("Ariel",22,"bold"))
    usernamelabel.grid(row=2,column=1,padx=20,pady=5)

    passwordlabel=Label(taz,text="Password",font=("Ariel",22,"bold"))
    passwordlabel.grid(row=3,column=1,padx=20,pady=5)

    userEntry=Entry(taz,textvariable=usernameVar,font=("Chiller",20,"bold"))
    userEntry.grid(row=2,column=2,padx=20,pady=5)

    passwordEntry=Entry(taz,show="*",textvariable=passwordVar,font=("Chiller",20,"bold"))
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton=Button(taz,text="Login",width=10,height=1,font=("Ariel",15,"bold"),fg="green",bd=10,command=adminLogin)
    loginButton.grid(row=5,column=1,columnspan=2,padx=20,pady=20)

################## welcome Window #############

def welcomeWindow():
    clear_screen()
    mainheading()
    welcome=Label(taz,text="Welcome Admin",font=("Ariel",25,"bold"))
    welcome.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    logoutButton=Button(taz,text="Logout",width=15,height=1,font=("Ariel",15,"bold"),fg="green",bd=10,command=logout)
    logoutButton.grid(row=4,column=1,columnspan=2,padx=20,pady=5)

    manageRest= Button(taz, text="Manage Item", width=15, height=1, font=("Ariel", 15, "bold"), fg="green", bd=10,
                         command=addItemWindow)
    manageRest.grid(row=5, column=1, columnspan=2, padx=20, pady=5)

    billGen= Button(taz, text=" Generate Bill ", width=15, height=1, font=("Ariel", 15, "bold"), fg="red", bd=10,
                         command=billWindow)
    billGen.grid(row=6, column=1, columnspan=2, padx=20, pady=5)

############## Back Button
def back():
    clear_screen()
    mainheading()
    welcomeWindow()
########################
def getItemInTreeview():
    # to delete already inserted data
    records=tazTV.get_children()
    for x in records:
        tazTV.delete(x)

    conn=pymysql.connect(host="localhost",user="root",db="hmsystem")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    query1="select * from itemlist"
    mycursor.execute(query1)
    data=mycursor.fetchall()
    #print(data)
    for row in data:
        tazTV.insert('','end',text=row['item_name'],values=(row["item_rate"],row["item_type"]))
    conn.close()

    tazTV.bind("<Double-1>",OnDoubleClick)
############### Double click###############
def OnDoubleClick(event):
    item=tazTV.selection()
    itemnameVar1=tazTV.item(item,"text")
    item_detail = tazTV.item(item, "values")
    itemnameVar.set(itemnameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])


#####################################
############### updateItem########
def updateItem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()

    dbconfig()
    que="update itemlist set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(que,val)
    coon.commit()
    messagebox.showinfo(" Updation  Confirmation ","Item Update Successfully")

    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()
############### Delete Item  ########
def deleteItem():
    id=itemId.get()
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()

    dbconfig()
    que1="delete from itemlist where item_name=%s"
    val=(name)
    mycursor.execute(que1,val)
    coon.commit()
    messagebox.showinfo(" Delete Confirmation ","Item Deleted Successfully")

    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()

##########################################
itemId=StringVar()
itemnameVar = StringVar()
itemrateVar=StringVar()
itemtypeVar=StringVar()

def addItemWindow():
    clear_screen()
    mainheading()
    insertItem=Label(taz,text="Insert Item",font=("Ariel",25,"bold"))
    insertItem.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    itemNameLabel=Label(taz,text="Item name",font=("Ariel",20,"bold"))
    itemNameLabel.grid(row=2,column=1,padx=20,pady=5)

    itemRateLabel = Label(taz, text="Item Rate (INR) ", font=("Ariel", 20, "bold"))
    itemRateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type", font=("Ariel", 20, "bold"))
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemNameEntry=Entry(taz,textvariable=itemnameVar,font=("Ariel",10,"bold"))
    itemNameEntry.grid(row=2,column=2,padx=20,pady=5)

    # for validation
    itemNameEntry.configure(validate="key",validatecommand=(callbackChar,"%P"))

    itemRateEntry = Entry(taz, textvariable=itemrateVar,font=("Ariel",10,"bold"))
    itemRateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemRateEntry.configure(validate="key", validatecommand=(callbackNum,"%P"))

    itemTypeEntry = Entry(taz, textvariable=itemtypeVar,font=("Ariel",10,"bold"))
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)
    itemTypeEntry.configure(validate="key", validatecommand=(callbackChar,"%P"))

    additemButton=Button(taz,text="Add Item",width=10,height=1,font=("Ariel",10,"bold"),fg="green",bd=10,command=additem)
    additemButton.grid(row=2,column=3,columnspan=1)

    updateButton = Button(taz, text="Update Item", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,
                           command=updateItem)
    updateButton.grid(row=3, column=3, columnspan=1)

    deleteButton = Button(taz, text="Delete Item", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,
                           command=deleteItem)
    deleteButton.grid(row=4, column=3, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=10, height=1, font=("Ariel", 10, "bold"),fg="green",bd=10,command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    backButton = Button(taz, text="Back", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,
                          command=back)
    backButton.grid(row=2, column=0, columnspan=1)

    # treeview

    tazTV.grid(row=6,column=0,columnspan=3)
    style=ttk.Style(taz)
    #style.theme_use('classic')
    style.theme_use('clam')
    style.configure("Treeview ",fieldbackground="green")
    scroolBar=Scrollbar(taz,orient="vertical",command=tazTV.yview)
    scroolBar.grid(row=6,column=2,sticky="NSE")


    tazTV.configure(yscrollcommand=scroolBar.set)
    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate ")
    tazTV.heading('#2', text="Type")


    getItemInTreeview()

#####################  Bill Generation ###########
global x
x=datetime.now()
datetimeVar =StringVar()
datetimeVar.set(x)
customerNameVar=StringVar()
contectNoVar=StringVar()
comboVar=StringVar()
baserateVar=StringVar()
qtyVar=StringVar()
costVar=StringVar()


########## Combo data ####
def combo_input():
    dbconfig()
    mycursor.execute('select item_name from itemlist')
    data=[]
    for row in mycursor.fetchall():
        data.append(row[0])

    return data
############## ,optionCallBack
def optionCallBack(*args):
    global itemname
    itemname=comboVar.get()
    aa=ratelist()
    print(aa)
    baserateVar.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j

############## optionCallBack2 ###

def optionCallBack2(*args):
    global qty
    qty=qtyVar.get()
    final=int(v)*int(qty)
    costVar.set(final)

############################
def ratelist():
    dbconfig()
    que2="select item_rate from itemlist where item_name=%s"
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    return data
############################################
def billWindow():
    clear_screen()
    mainheading()
    billItem=Label(taz,text=" Bill Generate ",font=("Ariel",25,"bold"))
    billItem.grid(row=1,column=1,columnspan=2,padx=50,pady=10)


    backButton = Button(taz, text="Back", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,command=back)
    backButton.grid(row=2, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    printButton = Button(taz, text="Print Bill", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,command=printBill)
    printButton.grid(row=4, column=0, columnspan=1)

    dateTimeLabel =Label(taz,text="Date & Time ",font=("Ariel",15,"bold"))
    dateTimeLabel.grid(row=2,column=1,padx=20,pady=5)

    dateTimeEntry=Entry(taz,textvariable=datetimeVar,font=("Ariel",15,"bold"))
    dateTimeEntry.grid(row=2,column=2,padx=20,pady=5)

    customerNameLabel =Label(taz,text="Customer Name ",font=("Ariel",15,"bold"))
    customerNameLabel.grid(row=3,column=1,padx=20,pady=5)
    customerNameEntry=Entry(taz,textvariable=customerNameVar,font=("Ariel",15,"bold"))
    customerNameEntry.grid(row=3, column=2, padx=20, pady=5)
    customerNameEntry.configure(validate="key", validatecommand=(callbackChar, "%P"))

    contactLabel =Label(taz,text="Contact No ",font=("Ariel",15,"bold"))
    contactLabel.grid(row=4,column=1,padx=20,pady=5)
    contactEntry = Entry(taz, textvariable=contectNoVar, font=("Ariel", 15, "bold"))
    contactEntry.grid(row=4, column=2, padx=20, pady=5)
    contactEntry.configure(validate="key", validatecommand=(callbackNum, "%P"))

    selectLabel =Label(taz,text=" Select Item ",font=("Ariel",15,"bold"))
    selectLabel.grid(row=5,column=1,padx=20,pady=5)


    l=combo_input()
    c=ttk.Combobox(taz,values=l,textvariable=comboVar,font=("Ariel",14,"bold"))
    c.set("Select Item")
    comboVar.trace('w',optionCallBack)
    c.grid(row=5,column=2,padx=20,pady=5)

    rateLabel =Label(taz,text="Item Rate ",font=("Ariel",15,"bold"))
    rateLabel.grid(row=6,column=1,padx=20,pady=5)

    rateEntry=Entry(taz,textvariable=baserateVar,font=("Ariel",15,"bold"))
    rateEntry.grid(row=6, column=2, padx=20, pady=5)

    qtyLabel =Label(taz,text="Item Qty ",font=("Ariel",15,"bold"))
    qtyLabel.grid(row=7,column=1,padx=20,pady=5)
    global qtyVar

    l = [1,2,3,4,5]
    qty = ttk.Combobox(taz, values=l, textvariable=qtyVar, font=("Ariel", 14, "bold"))
    qty.set("Select quantity")
    qtyVar.trace('w', optionCallBack2)
    qty.grid(row=7, column=2, padx=20, pady=5)



    costLabel =Label(taz,text="Cost ",font=("Ariel",15,"bold"))
    costLabel.grid(row=8,column=1,padx=20,pady=5)

    costEntry = Entry(taz, textvariable=costVar, font=("Ariel", 15, "bold"))
    costEntry.grid(row=8, column=2, padx=20, pady=5)

    billButton = Button(taz, text="Save Bill", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,
                          command=saveBill,bg="yellow")
    billButton.grid(row=9, column=2, columnspan=1)


############## save Bill #########
def saveBill():
    dt=datetimeVar.get()
    custname=customerNameVar.get()
    mobile=contectNoVar.get()
    item_name=itemname
    itemrate=v
    itemqty=qtyVar.get()
    total=costVar.get()

    dbconfig()
    insque="insert into `bill`(`datetime`, `customer_name`, `contect_no`, `item_name`, `item_rate`, `item_qty`, `cost`) values (%s,%s,%s,%s,%s,%s,%s)"
    val=(dt,custname,mobile,item_name,itemrate,itemqty,total)
    mycursor.execute(insque,val)
    coon.commit()
    messagebox.showinfo("Save data","Bill Saved successfully")
    customerNameVar.set("")
    contectNoVar.set("")
    itemnameVar.set("")
    baserateVar.set("")
    costVar.set("")
######## printBill #####

def printBill():
    clear_screen()
    mainheading()
    printItem = Label(taz, text=" Bill Details ", font=("Ariel", 25, "bold"))
    printItem.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    backButton = Button(taz, text="Back", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,command=back)
    backButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=10, height=1, font=("Ariel", 10, "bold"), fg="green", bd=10,command=logout)
    logoutButton.grid(row=1, column=3, columnspan=1)

    clickButton = Label(taz, text=" Double Click to TreeView to print Bill ", font=("Chiller", 15, "bold"))
    clickButton.grid(row=2,column=1,columnspan=2,padx=50,pady=10)

    tazTV1.grid(row=5,column=0,columnspan=4)
    style=ttk.Style(taz)
    # style.theme_use('classic')
    # style.theme_use('clam')
    # style.configure("Treeview ",fieldbackground="green")
    scroolBar=Scrollbar(taz,orient="vertical",command=tazTV1.yview)
    scroolBar.grid(row=5,column=8,sticky="NSE")

    tazTV1.configure(yscrollcommand=scroolBar.set)
    tazTV1.heading('#0', text="Date /Time")
    tazTV1.heading('#1', text="Name")
    tazTV1.heading('#2', text="Mobile")
    tazTV1.heading('#3', text="Selected Food ")
    tazTV1.heading('#4', text="Total cost")
    displayBill()

############# display Bill#############
def displayBill():
    # to delete already inserted data
    records = tazTV1.get_children()
    for x in records:
        tazTV.delete(x)

    conn = pymysql.connect(host="localhost", user="root", db="hmsystem")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query1 = "select * from bill"
    mycursor.execute(query1)
    data = mycursor.fetchall()
    #print(data)
    for row in data:
        tazTV1.insert('', 'end', text=row['datetime'], values=(row["customer_name"], row["contect_no"], row["item_name"], row["cost"]))
    conn.close()
    tazTV1.bind("<Double-1>", OnDoubleClick2)

############ onDoubleclick2 #
def OnDoubleClick2(event):
    item = tazTV1.selection()
    global itemnameVar11
    itemnameVar11 = tazTV1.item(item, "text")
    item_detail = tazTV1.item(item, "values")
    receipt()


################### recept ########

def receipt():
    billString=""
    billString+="======================= CAFETERIA BILL ======================\n\n"
    billString += "======================= Customer Details======================\n\n"

    dbconfig()
    query="select * from bill where datetime='{}';".format(itemnameVar11)
    mycursor.execute(query)
    data=mycursor.fetchall()
    #print(data)
    for row in data:
        billString+="{}{:<20}{:<10}\n".format("Date/Time","",row[1])
        billString += "{}{:<20}{:<10}\n".format("Customer Name", "", row[2])
        billString += "{}{:<20}{:<10}\n".format("Contact No.", "", row[3])

        billString += "\n======================= Item  Details======================\n"
        billString += "{:<20}{:<10}{:<25}{:<25}".format("Item Name","Rate ","Quantity","Total cost")
        billString+="\n {:<20}{:<10}{:<25}{:<25}".format(row[4],row[5],row[6],row[7])
        billString += "\n=============================================\n"
        billString+="{}{:<10}{:<15}{:10}\n".format("Total Amount "," "," ",row[7])
        billString += "                               Include all taxes \n"

        billString+="\n \n==============  THANKS PLEASE VISIT AGAIN  =============\n"

    billFile=filedialog.asksaveasfile(mode="w",defaultextension=".txt" , initialfile=row[2])
    if billFile is None:
        messagebox.showerror("File Name error","Invalid File Name")
    else:
        billFile.write(billString)
        billFile.close()

#################################################
def additem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()

    dbconfig()
    query="insert into itemlist (item_name,item_rate,item_type) values (%s,%s,%s)"
    val=(name,rate,type)
    mycursor.execute(query,val)
    coon.commit()
    messagebox.showinfo("Save Item","item Saved Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()

def adminLogin():
    dbconfig()
    usename=usernameVar.get()
    password=passwordVar.get()
    que="select * from user_info where userid=%s and pass=%s"
    val=(usename,password)
    mycursor.execute(que,val)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True
    coon.close()
    if flag==True:
        welcomeWindow()
    else:
        messagebox.showerror("Invalid user credential","Either use name or password in correct")
        usernameVar.set("")
        passwordVar.set("")


mainheading()
loginwindow()

taz.title("CAFETERIA BILLING SYSTEM ")

taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()