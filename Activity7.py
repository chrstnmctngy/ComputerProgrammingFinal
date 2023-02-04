from tkinter import *

root = Tk()
root.geometry("250x100")

myLbl_num = Label(root, text="Enter first number")
myLbl_num.grid(row= 0, column=0)

myInput_num = Entry(root, width=20)
myInput_num.grid(row= 0, column=1)
myInput_num.get()

myLbl_num1 = Label(root, text="Enter second number")
myLbl_num1.grid(row= 1, column=0)

myInput_num1 = Entry(root, width=20)
myInput_num1.grid(row= 1, column=1)
myInput_num1.get()

def add():
    result = int(myInput_num.get())+ int(myInput_num1.get())
    myLbl_txt = Label(root,  text="Result: " + str(result))
    myLbl_txt.grid(row= 3, column=1)

myBtn_txt = Button(root, text="Compute Sum", command=add)
myBtn_txt.grid(row= 2, column=1)

root.mainloop()
