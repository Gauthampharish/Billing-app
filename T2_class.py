import mysql.connector as sq

from tkinter import *
from tkinter.ttk import Combobox, Treeview


mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                   auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("hnksadk")
my = mycon.cursor()


class T2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        subframe = Frame(self, bd=10, bg='white')
        subframe.place(x=10, y=200, height=500, width=1500)

        scrollbar_order_x = Scrollbar(subframe, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(subframe, orient=VERTICAL)

        order_tabel = Treeview(subframe,
                               columns=("BIll No", "AMOUNT", "DATE OF BILLING"),
                               xscrollcommand=scrollbar_order_x.set,
                               yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("BIll No", text="BIll No")
        order_tabel.heading("AMOUNT", text="Rate")
        order_tabel.heading("DATE OF BILLING", text="Quantity")

        order_tabel["displaycolumns"] = ("BIll No", "AMOUNT", "DATE OF BILLING")
        order_tabel["show"] = "headings"
        order_tabel.column("AMOUNT", width=200, anchor='center', stretch=NO)
        order_tabel.column("DATE OF BILLING", width=200, anchor='center', stretch=NO)

        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        def table():

            sa = self.controller.get_page(User)
            ka = sa.username.get()

            query = "select * from {tab}".format(tab=ka)
            my.execute(query)
            l = []
            c = my.fetchall()
            for w in c:
                l.append(w)
                print(l)
                for j in range(0, len(l)):
                    order_tabel.insert("", 'end', text="L1", values=(l[j][0], l[j][1], l[j][2]))

        order_tabel.pack(fill=BOTH, expand=1)
        buttontoget = Button(self, text='GET', command=lambda: [table()])
        buttontoget.place(x=30, y=10)
        bakbuttontranspage = Button(self, text='Back', command=lambda: [transbackpagecm()])
        bakbuttontranspage.place(x=80, y=10)

        def transbackpagecm():
            controller.show_frame(Mainpage)
