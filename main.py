import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Activity 4")
root.geometry("500x500")

Label(root, text="Student ID").place(x=10, y=10)
v1 = tk.Entry(root)
v1.place(x=140, y=10)

Label(root, text="First Name").place(x=10, y=40)
v2 = tk.Entry(root)
v2.place(x=140, y=40)

Label(root, text="Last Name").place(x=10, y=70)
v3 = tk.Entry(root)
v3.place(x=140, y=70)

Label(root, text="Email").place(x=10, y=100)
v4 = tk.Entry(root)
v4.place(x=140, y=100)

Label(root, text="Password").place(x=10,y=130)
v5 = tk.Entry(root)
v5.place(x=140, y=130)



def GetValue(event):
    v1.delete(0, END)
    v2.delete(0, END)
    v3.delete(0, END)
    v4.delete(0, END)
    v5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    v1.insert(0,select['studentid'])
    v2.insert(0,select['fname'])
    v3.insert(0,select['lname'])
    v4.insert(0,select['email'])
    v5.insert(0,select['password'])

def addValue():
    studentid = v1.get()
    fname = v2.get()
    lname = v3.get()
    email = v4.get()
    password = v5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="dbactivity4")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO tbluser (studentid, fname, lname, email, password) VALUES (%s,%s,%s,%s,%s)"
        val = (studentid, fname, lname, email, password)
        mycursor.execute(sql, val)
        mysqldb.commit()

        lastid = mycursor.lastrowid

        messagebox.showinfo("information", "Record inserted successfully...")
        v1.delete(0, END)
        v2.delete(0, END)
        v3.delete(0, END)
        v4.delete(0, END)
        v1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def updValue():
    studentid = v1.get()
    fname = v2.get()
    lname = v3.get()
    email = v4.get()
    password = v5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="dbactivity4")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  registation set fname= %s,lname= %s,email= %s,password= %s where studentid= %s"
       val = (studentid, fname, lname, email, password)
       mycursor.execute(sql, val)
       mysqldb.commit()

       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       v1.delete(0, END)
       v2.delete(0, END)
       v3.delete(0, END)
       v4.delete(0, END)
       v5.delete(0, END)
       v1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delValue():
    studentid = v1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="dbactivity4")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from tbluser where id = %s"
       val = (studentid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       v1.delete(0, END)
       v2.delete(0, END)
       v3.delete(0, END)
       v4.delete(0, END)
       v5.delete(0, END)
       v1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="dbactivity4")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT studentid,fname,lname,email,password FROM tbluser")
        tbluser = mycursor.fetchall()
        print(tbluser)
 
        for i, (studentid,fname,lname,email,password) in enumerate(tbluser, start=1):
            listBox.insert("", "end", values=(studentid, fname, lname, email, password))
            mysqldb.close()

addButton = Button(root, text="Add", command=addValue, height=2, width=7).place(x=50, y=180)
updButton = Button(root, text="Update", command=updValue, height=2, width=7).place(x=120, y=180)
delButton = Button(root, text="Delete", command=delValue, height=2, width=7).place(x=190, y=180)

cols = ('studentid', 'fname', 'lname','email', 'password')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=230)
 
show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()