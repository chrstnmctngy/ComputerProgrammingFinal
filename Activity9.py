from tkinter import *

root = Tk()
root.geometry("320x320")
root.title("Activity 9 - Macatangay")
root.config(bg="#68A7AD")
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.columnconfigure(4, weight=2)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

myLbl_name = Label(root, text="Submitted By: Christian R. Macatangay", font="Helvetica 10 bold", bg="#68A7AD")
myLbl_name.grid(row=1, column=0, columnspan=4, pady=20, sticky=N)

myLbl_style = Label(root, text="", bg="#ffffff", relief="solid", height=3, width=50)
myLbl_style.grid(row=2, column=0, columnspan=4)

myLbl_num = Label(root, text="Enter first number", font="Helvetica 10 bold", bg="#68A7AD")
myLbl_num.grid(row=3, column=0, columnspan=4, padx=17, pady=10, sticky=W)

myInput_num = Entry(root, width=20, bd=1, highlightthickness=1)
myInput_num.grid(row=4, column=0, columnspan=4, padx=15, pady=10, ipady=3, sticky=W)
myInput_num.get()

myLbl_num1 = Label(root, text="Enter second number", font="Helvetica 10 bold", bg="#68A7AD")
myLbl_num1.grid(row=3, column=2, columnspan=4, padx=7, pady=10, sticky=E)

myInput_num1 = Entry(root, width=20, bd=1, highlightthickness=1)
myInput_num1.grid(row=4, column=2, columnspan=4, padx=15, pady=10, ipady=3, sticky=E)
myInput_num1.get()

def add():
    rslt = int(myInput_num.get()) + int(myInput_num1.get())
    myLbl_txt = Label(root,  text="" + str(rslt), font="Arial 16 bold", bg="#ffffff")
    myLbl_txt.grid(row=2, column= 0, columnspan=4, pady=10, sticky=N)

def sub():
    rslt = int(myInput_num.get()) - int(myInput_num1.get())
    myLbl_txt1 = Label(root,  text="" + str(rslt), font="Arial 16 bold", bg="#ffffff")
    myLbl_txt1.grid(row=2, column= 0, columnspan=4, pady=10, sticky=N)

def mul():
    rslt = int(myInput_num.get()) * int(myInput_num1.get())
    myLbl_txt2 = Label(root,  text="" + str(rslt), font="Arial 16 bold", bg="#ffffff")
    myLbl_txt2.grid(row=2, column= 0, columnspan=4, pady=10, sticky=N)  

def div():
    rslt = float(myInput_num.get()) / float(myInput_num1.get())
    dcml = ("%.2f" % rslt)
    myLbl_txt3 = Label(root,  text="" + str(dcml), font="Arial 16 bold", bg="#ffffff")
    myLbl_txt3.grid(row=2, column= 0, columnspan=4, pady=10, sticky=N)

def clear():
    myInput_num.delete(0, END)
    myInput_num1.delete(0, END)
    ttl = Label(root, text="")
    ttl.config(bg="#ffffff", height=2, width= 30)
    ttl.grid(row=2, column=0, columnspan=4)

myBtn_txt = Button(root, text=" + ", font="Arial 12 bold", bg="#E5CB9F", height=2 , width=4, command=add)
myBtn_txt.grid(row=5, column=0, padx=10, pady=10)

myBtn_txt = Button(root, text=" - ", font="Arial 12 bold", bg="#E5CB9F", height=2 , width=4, command=sub)
myBtn_txt.grid(row=5, column=1, padx=10, pady=10)

myBtn_txt = Button(root, text=" * ", font="Arial 12 bold", bg="#E5CB9F", height=2 , width=4, command=mul)
myBtn_txt.grid(row=5, column=2, padx=10, pady=10)

myBtn_txt = Button(root, text=" / ", font="Arial 12 bold", bg="#E5CB9F", height=2 , width=4, command=div)
myBtn_txt.grid(row=5, column=3, padx=10, pady=10)

myBtn_clear = Button(root, text=" Clear ", font="Helvetica 10 bold", bg="#E5CB9F", height=2 , width=35, command=clear)
myBtn_clear.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky=S)

root.mainloop()
