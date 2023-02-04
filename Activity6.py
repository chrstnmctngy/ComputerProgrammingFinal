from tkinter import *

root = Tk()
root.geometry("300x200")


myLbl_num = Label(root, text="Enter first number")
myLbl_num.pack()

myInput_num = Entry(root, width=20)
myInput_num.pack()
myInput_num.get()

myLbl_num1 = Label(root, text="Enter second number")
myLbl_num1.pack()

myInput_num1 = Entry(root, width=20)
myInput_num1.pack()
myInput_num1.get()

def add():
    result = int(myInput_num.get())+ int(myInput_num1.get())
    myLbl_txt = Label(root,  text="Result: " + str(result))
    myLbl_txt.pack()

myBtn_txt = Button(root, text="Compute Sum", command=add)
myBtn_txt.pack()

root.mainloop()
