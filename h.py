"""
'''import mysql.connector as sq
mycon= sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",auth_plugin='mysql_native_password')
if mycon.is_connected():
        print("hnksadk")
a= input()
my = mycon.cursor()
#cre = ""CREATE TABLE {tab} (Sl_No INT(200),NAME CHAR(20))"".format(tab=a)
my.execute(cre)
mycon.commit()
print('add')



from tkinter import*
from tkinter import ttk
import datetime

import mysql.connector as sq
# fn to get Mrp
def sqlprod(h):
    productnameget2=h
    b = productnameget2.lower()

    x = "select mrp from productdetails where product='{}'".format(b)
    my.execute(x)
    y = my.fetchall()
    if y != []:

        for i in y:
            for j in i:
                print(j)
                mrpv = j
                mrpvalue.set(mrpv)
                gd = " "
                messagevar.set(gd)
        a = 'true'
        return a


    else:

        x = "no such product exist"
        messagevar.set(x)
        b = 'false'
        return b

#what shd happen after billing is done
def afterbill():
    global list1
    global list3
    list1=[]
    list3=[]
    grandtotalfn()
    totalamt.set(0)
    mrpvalue.set(0)

#how bill window shd look like
def billwindow():

    if list1!=[]:


            st = "-" * 61 + "BILL" + "-" * 61 + "\nDate:- "


            x=billnumbervar.get()
            st += f"\nBillnumber:- {x}\n"
            st += "-" * 130 + "\n" + " " * 4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
            st += "-" * 130 + "\n"
            for i in range(0,len(list3)):

                    name = list1[i][0]
                    rate = list1[i][1]
                    quantity = list1[i][2]
                    price = list1[i][3]
                    st += name + "\t\t\t\t\t" + str(rate) + "\t      " +str(quantity) + "\t\t  " + str(price) + "\n\n"
            st += "-" * 130
            st += f"\n\t\t\tTotal price : {Grandtotalvalue.get()}\n"
            st += "-" * 130



            file = open(f"bill records\\{x}.txt", "w+")
            file.write(st)
            file.close()
            file = open(f"bill records\\{x}.txt", "r")

            read=file.readlines()
            bill = Toplevel()
            bill.title("Bill")
            bill.geometry("670x500+300+100")

            bill_text_area = Text(bill, font=("arial", 12))
            bill_text_area.insert(1.0, st)
            bill_text_area.pack(expand=True, fill=BOTH)
            order_tabel.delete(*order_tabel.get_children())
            afterbill()


    else:
        t="please enter items "
        messagevar.set(t)



#to disp grandtotal
def grandtotalfn():
    a=0
    for i in range(0,len(list3)):
        a=a+list3[i]
    Grandtotalvalue.set(a)

#to upadte mrp of products
def updatesql():
    z=productupdate.get()
    if sqlprod(z) == 'true':
        y=mrpupdate.get()
        x='Update productdetails set mrp={} where product ="{}"'.format(y,z)
        my.execute(x)
        mycon.commit()
        x = "Mrp  updated"
        messagevarb.set(x)
    else:
        x = "Mrp could not be updated"
        messagevarb.set(x)

# to add products
def addsql():
    z = productupdate1.get()
    if sqlprod(z) == 'true':
        y = mrpupdate1.get()
        x='insert into productdetails  Values("{}",{})'.format(z,y)
        my.execute(x)
        mycon.commit()
        x = "Product  added"
        messagevarb.set(x)
    else:
        x="Product could not be added"
        messagevarb.set(x)

# to delete product
def delsql():
    z = productupdate2.get()
    if sqlprod(z)=='true':


        x="delete from productdetails where product='{}'".format(z)
        my.execute(x)
        mycon.commit()
        x = "Product deleted"
        messagevarb.set(x)
    else:
        x = "Product could not be deleted"
        messagevarb.set(x)


# the tree view
def Tablev():

    global count
    b = productname.get()
    d = str(quantity.get())
    h = str(totalamt.get())
    c = str(mrpvalue.get())


    order_tabel.insert("", 'end', text="L1",values=(b, c, d, h))
    count = count + 1



#clear tree view
def delete():
    order_tabel.delete(*order_tabel.get_children())








#to get total of the product (mrp* quantity)

def total():

    x=int(quantity.get())
    b=mrpvalue.get()
    if quantity.get()==0:
        y="Pls enter the quantity"
        messagevar.set(y)
    else:
        totalno=b*x
        print(totalno)
        totalamt.set(totalno)
# to get the list to add details into final bill
def billlistadd():

    if productnamechk()=='true':
        global list1
        global list2
        if quantity.get()==0:
            x="Pls enter the quantity"
            messagevar.set(x)



        else:
            x = int(quantity.get())
            b = mrpvalue.get()
            totalno = b * x
            print(totalno)
            totalamt.set(totalno)




            list11=[productname.get(),mrpvalue.get(),quantity.get(),totalamt.get()]
            list1.append(list11)
            list2.append(list11)
            h=totalno
            list3.append(h)
            print(list3)
            Tablev()
            print(list1)

            gd = " "
            messagevar.set(gd)
            grandtotalfn()






def finalbill():
    global list2,list1
    for i in list1:
        list2.append(i)
    print(list2)
#checking whether product exists
def productnamechk():

    productnameget=productname.get()
    b=productnameget.lower()

    x = "select mrp from productdetails where product='{}'".format(b)
    my.execute(x)
    y = my.fetchall()
    if y != []:

        for i in y:
            for j in i:
                print(j)
                mrpv=j
                mrpvalue.set(mrpv)
                gd=" "
                messagevar.set(gd)
        a = 'true'
        return a


    else:

        x="no such product exist"
        messagevar.set(x)
        b = 'false'
        return b







from  datetime import *
def dat():
    a=datetime.now()
    return a
# main window
Main =Tk()
Main.title("Main window")
Main.geometry('1800x900')
Main.configure(bg='white')
tabControl = ttk.Notebook(Main,width=1500,height=750)
# listing al variables
count=0
billnumbervar=StringVar()
productname=StringVar(
quantity=IntVar()
totalamt=IntVar()
Grandtotalvalue=IntVar()
mrpvalue=IntVar()
messagevarb=StringVar()
messagevar=StringVar()
mrpupdate=IntVar()
mrpupdate1=IntVar()
productupdate=StringVar()
productupdate1=StringVar()
productupdate2=StringVar()

mycon = sq.connect(host="localhost", user="root", password='Edgbaston@2019', database="billing",auth_plugin='mysql_native_password')
if mycon.is_connected():
        print("hnksadk")
my = mycon.cursor()

#creating tab
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1,text='Billing')
tabControl.add(tab2,text='Setting')
c=Canvas(tab1,bg='white',height=750,width=1500).place(x=1,y=1)
h=Canvas(tab2,bg='white',height=750,width=1500).place(x=1,y=1)
tabControl.place(x=10, y=0)
list1=[]
list2=[("product","Mrp","Quantity",'Total')]
total_rows=len(list2)
total_columns = len(list2[0])
list3=[]







# the bill scene
Bill=Label(tab1,text='Bill Number',fg='Black',bg="white",font=('Times new roman',22,"bold")).place(x=700,y=30)
date=Label(tab1,text=dat(),fg='black',bg="white",font=('Times new roman',20,"bold")).place(x=180,y=30)
date1=Label(tab1,text='Date and Time:',fg='black',bg="white",font=('Times new roman',22,"bold")).place(x=12,y=30)
billnumber=Entry(tab1,width=15,textvariable=billnumbervar,bg="white",font=('arial',16)).place(x=900,y=30)
nameofpro=Label(tab1,text='Product',fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=12,y=75)
Mrp=Label(tab1,text="Mrp",fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=250,y=75)
quantiylabel=Label(tab1,text='Quantity',fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=500,y=75)
Total=Label(tab1,text='Total',fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=730,y=75)
producttext=Entry(tab1,width=15,textvariable=productname,bg="white",font=('arial',16)).place(x=5,y=150,height=30)
mrpla=Label(tab1,textvariable=mrpvalue,fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=260,y=150)
quantityentry = Entry(tab1,width=15,bg="white",textvariable=quantity,font=('arial',16)).place(x=485,y=150,height=30)
totalentry=Label(tab1,textvariable=totalamt,bg="white",font=('arial',16,"bold")).place(x=770,y=150)
order_frame = Frame(tab1,bd=8, bg="white")
order_frame.place(x=12,y=300,height=500,width=1000)

#Order Tabel

order_tabel_frame = Frame(order_frame)
order_tabel_frame.place(x=0,y=0,height=500,width=1000)

scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

order_tabel = ttk.Treeview(order_tabel_frame,
            columns =("name","rate","quantity","Total"),xscrollcommand=scrollbar_order_x.set,
            yscrollcommand=scrollbar_order_y.set)

order_tabel.heading("name",text="Name")
order_tabel.heading("rate",text="Rate")
order_tabel.heading("quantity",text="Quantity")
order_tabel.heading("Total",text="Total")
order_tabel["displaycolumns"]=("name", "rate","quantity","Total")
order_tabel["show"] = "headings"
order_tabel.column("rate",width=200,anchor='center', stretch=NO)
order_tabel.column("quantity",width=200,anchor='center', stretch=NO)
order_tabel.column("Total",width=200,anchor='center', stretch=NO)



scrollbar_order_x.pack(side=BOTTOM,fill=X)
scrollbar_order_y.pack(side=RIGHT,fill=Y)

scrollbar_order_x.configure(command=order_tabel.xview)
scrollbar_order_y.configure(command=order_tabel.yview)

order_tabel.pack(fill=BOTH,expand=1)

# Labels and butttons

pay=Button(tab1,text='pay',width=10,font=('timesnewroman,16'),command=lambda:[billwindow()],bg="white").place(x=900,y=150)
add=Button(tab1,text='add',width=10,command=lambda:[billlistadd()],font=('timesnewroman,16'),bg="white").place(x=900,y=185)

Grandtotal=Label(tab1,text='Grandtotal',fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=1110,y=600)
Grandtotallabel=Label(tab1,textvariable=Grandtotalvalue,fg='black',bg="white",font=('Times new roman',30,"bold")).place(x=1310,y=600)
Messagelabel=Label(tab1,textvariable=messagevar,fg='black',bg="white",font=('Times new roman',20,"bold")).place(x=1150,y=200)
deletebutton=Button(tab1,text='Delete',width=10,command=lambda:[delete()],font=('timesnewroman,16'),bg="white").place(x=900,y=225)

#settings tab
#update frame
update = Frame(tab2,bd=8, bg="black")
update.place(x=5 ,y=20,height=300,width=300)
Update1=Label(update,text="Update",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=80,y=5)
Product = Label(update,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=65)
Mrp=Label(update,text="Mrp",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=125)
Update=Button(update,text="Update",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[updatesql()]).place(x=80,y=195)
Productentry=Entry(update,width=10,bg="white",textvariable=productupdate,font=('arial',16)).place(x=150,y=70,height=30)
mrpentry=Entry(update,width=10,bg="white",textvariable=mrpupdate,font=('arial',16)).place(x=150,y=130,height=30)

#add frame
insertproduct= Frame(tab2,bd=8, bg="black")
insertproduct.place(x=1000 ,y=20,height=300,width=300)
productadd=Label(insertproduct,text="Add Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=65,y=5)
producttext=Label(insertproduct,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=65)
Mrpn=Label(insertproduct,text="Mrp",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=125)
mrpaddentry=Entry(insertproduct,width=10,bg="white",textvariable=mrpupdate1,font=('arial',16)).place(x=150,y=130,height=30)
productentry=Entry(insertproduct,width=10,textvariable=productupdate1,font=('arial',16)).place(x=150,y=70,height=30)
addproduct=Button(insertproduct,text="Add",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[addsql()]).place(x=80,y=195)
# delete frame
deleteproduct= Frame(tab2,bd=8, bg="black")
deleteproduct.place(x=500 ,y=20,height=300,width=300)
productdelete=Label(deleteproduct,text="Delete",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=80,y=5)
deletep=Label(deleteproduct,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=85)
productentry=Entry(deleteproduct,width=10,textvariable=productupdate2,font=('arial',16)).place(x=150,y=85,height=30)
deleteproductbu=Button(deleteproduct,text="Delete",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[delsql()]).place(x=80,y=195)
Messagelabel1=Label(tab2,textvariable=messagevarb,fg='black',bg="white",font=('Times new roman',20,"bold")).place(x=600,y=500)

Main.mainloop()

from tkinter.ttk import Combobox,Treeview

import mysql.connector as sq
from tkinter import ttk
from tkinter import *
mycon= sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",auth_plugin='mysql_native_password')
if mycon.is_connected():
        print("hnksadk")
my = mycon.cursor()
root = Tk()
columns = ("Items",'Quantity',"Mrp",'Total')
Treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  #

Treeview.column("Items", width=200, anchor='center')
Treeview.column("Quantity", width=200, anchor='center')
Treeview.column("Mrp", width=270, anchor='center')
Treeview.column("Total", width=300, anchor='center')

Treeview.heading("Items", text="Items")
Treeview.heading("Quantity", text="Values")
Treeview.heading("Quantity", text="Values")
Treeview.heading("Total", text="Values")


Treeview.pack(side=LEFT, fill=BOTH)
l=[]
name = []
ipcode = []
iquantity=[]
itotal=[]
cn=0
rn=0


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


def set_cell_value(event):
    global cn
    global rn

    def Convert(tup, di):
        di = dict(tup)
        return di
    for item in Treeview.selection():

        item_text = Treeview.item(item, 'values')
        column = Treeview.identify_column(event.x)

        row = Treeview.identify_row(event.y)
        print(column, row)

    producetquery="select * from productdetails"
    my.execute(producetquery)
    l=my.fetchall()
    l1=[]
    d={}
    d=(Convert(l, d))
    print(d)
    c=d.keys()
    for i in c:
        l1.append(i)
    comboBox = Combobox(root, values=l1)
    comboBox.place(x=3, y=6 + rn * 20)


    entryedit2=Text(root,width=24,height=1)
    entryedit2.place(x=200,y=6 + rn * 20)


    def saveedit():
        Treeview.set(item, column=column, value=comboBox.get())
        l.append(comboBox.get())
        print(l)
        Treeview.set(item, column=column, value=entryedit2.get(0.0, "end"))

        comboBox.destroy()
        okb.destroy()

    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    okb.place(x=90 , y=2 + rn * 20)


def newrow():
    global rn
    name.append('to be named')
    ipcode.append('value')
    itotal.append('hello')
    iquantity.append('bye')

    Treeview.insert('', len(name) - 1, values=(name[len(name) - 1], ipcode[len(name) - 1],iquantity[len(name) - 1],itotal[len(name) - 1]))
    Treeview.update()

    newb.place(x=120, y=(len(name) - 1) * 20 + 45)
    newb.update()
    rn=rn+1


Treeview.bind('<Double-1>', set_cell_value)
newb = ttk.Button(root, text='new item', width=20, command=newrow)
newb.place(x=120, y=(len(name) - 1) * 20 + 45)

for col in columns:
    Treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(Treeview, _col, False))


root.mainloop()

l2=[]
s=0
for i in a:
    l.append(i)
for j in b:
    l2.append(j)
if len(l)==len(l2):
    for i in range(0,len(l)):
        if l[i] != l2[i]:
            s=s+2
        else:
            continue
else:
    print("charnotequal")
print(s)
\
def keyworddigit(digit):
    if digit == 'NQA':
        a = 1
        return a
    elif digit == 'CA':
        a = 2
        return a
    elif digit == "WA":
        return 3
    elif digit == "NAS":
        return 4
    elif digit == "NAT":
        return 5


def total(k):
    global d
    a = k[2]

    totalmarks = (int(k[2]) * 5) + (-3 * int(k[3])) + (-1 * int(k[4])) + (0 * int(k[5]))

    d[k[0]] = totalmarks


def inputuserde(p, q, r):
    indexoflist = keyworddigit(q)
    achu = int(indexoflist)

    for i in range(1, len(l1)):
        gautham = l1[i][achu]

        if p == "G":

            if int(gautham) > int(r):
                print(l1[i][0])

        elif p == "GE":
            if int(gautham) >= int(r):
                print(l1[i][0])
        elif p == "L":
            if int(gautham) < int(r):
                print(l1[i][0])
        elif p == "LE":
            if int(gautham) <= int(r):
                print(l1[i][0])
        elif p == "E":
            if int(gautham) == int(r):
                print(l1[i][0])


f = open("exam.txt", 'r')
l1 = []
d = {}
readfile = f.readlines()
for i in readfile:
    l = []
    for j in i.split():
        l.append(j)
    l1.append(l)

for m in range(1, len(l1)):
    chumma = total(l1[m])

keyword, markdetails, valueneed = input().split()
try:
    hello = inputuserde(keyword, markdetails, valueneed)
except:
    print("l")

"""
