import mysql.connector as sq
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox, Treeview

mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                       auth_plugin='mysql_native_password')
if mycon.is_connected():
        print("setting")
my = mycon.cursor()


class Settingpage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        mrpupdate=IntVar()
        mrpupdate1=IntVar()
        productupdate=StringVar()
        productupdate1=StringVar()
        productupdate2=StringVar()
        def sqlprod(h):
                productnameget2=h
                b = productnameget2.lower()

                x = "select mrp from productdetails where productname='{}'".format(b)
                my.execute(x)
                y = my.fetchall()
                if y != []:

                    for i in y:
                        for j in i:
                            print(j)
                            mrpv = j
                            #mrpvalue.set(mrpv)
                            gd = " "
                            #messagevar.set(gd)
                    a = 'true'
                    return a


                else:

                    x = "no such product exist"
                   # messagevar.set(x)
                    b = 'false'
                    return b
       # to add products
        def addsql():
            try:

                z = productupdate1.get()
                
                y = mrpupdate1.get()
                print("c")
                x='insert into productdetails  Values("{}",{})'.format(z,y)
                my.execute(x)
                mycon.commit()
                print("Product  added")
                #messagevarb.set(x)
            except :
                 x="Product could not be added"
                 #messagevarb.set(x)
            
        # to delete product
        def delsql():
            z = productupdate2.get()
            if sqlprod(z)=='true':


                x="delete from productdetails where productname='{}'".format(z)
                my.execute(x)
                mycon.commit()
                print("Product deleted")
                #messagevarb.set(x)
            else:
                x = "Product could not be deleted"
                #messagevarb.set(x)

        def updatesql():
            z=productupdate.get()
            if sqlprod(z) == 'true':
                y=mrpupdate.get()
                x='Update productdetails set mrp={} where productname ="{}"'.format(y,z)
                my.execute(x)
                mycon.commit()
                print( "Mrp  updated")
               ##messagevarb.set(x)
            else:
                x = "Mrp could not be updated"
                #messagevarb.set(x)
        insertproduct= Frame(self,bd=8, bg="black")
        insertproduct.place(x=1000 ,y=20,height=300,width=300)
        productadd=Label(insertproduct,text="Add Product",fg='black',bg='white',font=('Times new roman',22,"bold"))
        productadd.place(x=65,y=5)
        producttext=Label(insertproduct,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold"))
        producttext.place(x=3,y=65)
        Mrpn=Label(insertproduct,text="Mrp",fg='black',bg='white',font=('Times new roman',22,"bold"))
        Mrpn.place(x=3,y=125)
        addproduct=Button(insertproduct,text="Add",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[addsql()])
        addproduct.place(x=80,y=195)
        mrpaddentry=Entry(insertproduct,width=10,bg="white",textvariable=mrpupdate1,font=('arial',16))
        mrpaddentry.place(x=150,y=130,height=30)
        productentry=Entry(insertproduct,width=10,textvariable=productupdate1,font=('arial',16))
        productentry.place(x=150,y=70,height=30)

        # delete frame
        deleteproduct= Frame(self,bd=8, bg="black")
        deleteproduct.place(x=500 ,y=20,height=300,width=300)
        productdelete=Label(deleteproduct,text="Delete",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=80,y=5)
        deletep=Label(deleteproduct,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=85)
        productentry=Entry(deleteproduct,width=10,textvariable=productupdate2,font=('arial',16)).place(x=150,y=85,height=30)
        deleteproductbu=Button(deleteproduct,text="Delete",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[delsql()]).place(x=80,y=195)
       
        #update frame
        update = Frame(self,bd=8, bg="black")
        update.place(x=5 ,y=20,height=300,width=300)
        Update1=Label(update,text="Update",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=80,y=5)
        Product = Label(update,text="Product",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=65)
        Mrp=Label(update,text="Mrp",fg='black',bg='white',font=('Times new roman',22,"bold")).place(x=3,y=125)
        Update=Button(update,text="Update",fg='black',bg='white',font=('Times new roman',22,"bold"),command=lambda:[updatesql()]).place(x=80,y=195)
        Productentry=Entry(update,width=10,bg="white",textvariable=productupdate,font=('arial',16)).place(x=150,y=70,height=30)
        mrpentry=Entry(update,width=10,bg="white",textvariable=mrpupdate,font=('arial',16)).place(x=150,y=130,height=30)