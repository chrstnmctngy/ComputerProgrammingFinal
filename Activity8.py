from tkinter import *

root = Tk()
root.geometry("395x100")
root.config(bg="#68A7AD")

myLbl_num = Label(root, text="Enter first number", font="Helvetica, 10", bg="#68A7AD")
myLbl_num.place(x= 10, y=11)

myInput_num = Entry(root, width=20)
myInput_num.place(x= 145, y=12.5)
myInput_num.get()

myLbl_num1 = Label(root, text="Enter second number", font="Helvetica, 10", bg="#68A7AD")
myLbl_num1.place(x= 10, y=36)

myInput_num1 = Entry(root, width=20)
myInput_num1.place(x= 145, y=37.5)
myInput_num1.get()

def add():
    result = int(myInput_num.get())+ int(myInput_num1.get())
    myLbl_txt = Label(root,  text="Result: "+ str(result), font="Helvetica 10 bold", fg="#630606", bg="#68A7AD")
    myLbl_txt.place(x= 10, y=62.5)

myBtn_txt = Button(root, text="Compute Sum", font="Helvetica 10 bold", bg="#E5CB9F", command=add)
myBtn_txt.place(x= 280, y=20)

root.mainloop()
