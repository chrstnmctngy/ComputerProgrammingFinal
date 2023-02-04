from tkinter import *

root = Tk()

root.geometry("500x390")
root.title("Activity 10 - Macatangay")
root.config(bg="#97BFB4")

def pin():
    myPin = int(myInput_num.get())
    
    if myPin == 2222:
        myLbl_wel.config(text="Welcome, Christian", font=("Helvetica", 14, "bold"))
        myLbl_wel.grid(row=1, column=2, padx=23)
    else:
        myLbl_wel.config(text="Welcome, Unknown", font=("Helvetica", 14, "bold"))
        myLbl_wel.grid(row=1, column=2, padx=20)

    myLbl_curbal.config(text="Current Balance:", font=("Helvetica", 12, "bold"))
    myLbl_curbal.grid(row=2, column=2, padx=20)

    myFrm_curbal.config(bg="#ffffff", relief="solid", bd=1, height=3, width=34)
    myFrm_curbal.grid(row=3, column=2)

    myInput_num.delete(0, END)

    myBtn_wel.config(state=DISABLED)
    myBtn_initbal.config(state=NORMAL)

def initbal(): 
    global myInput
    myInput = int(myInput_num.get())
    myLbl_initbal.config(text="", bg="#ffffff", width=10, font=("Helvetica", 14, "bold"), fg="#4F091D")
    myLbl_initbal.grid(row=3, column=2, padx=23)
    
    myInput_num.delete(0, END)

    myBtn_initbal.config(state=DISABLED)
    myBtn_rembal.config(state=NORMAL)
    myBtn_deposit.config(state=NORMAL)
    myBtn_withdraw.config(state=NORMAL)

def rembal():
    myLbl_rembal.config(text=myInput, bg="#ffffff", width=10, font=("Helvetica", 14, "bold"), fg="#4F091D")
    myLbl_rembal.grid(row=3, column=2, padx=23)

def deposit():
    myInput1 = int(myInput_num.get())
    global myDepo
    myDepo = myInput + myInput1
    myLbl_deposit.config(text=myDepo, bg="#ffffff", width=10, font=("Helvetica", 14, "bold"), fg="#4F091D")
    myLbl_deposit.grid(row=3, column=2, padx=23)

    myInput_num.delete(0, END)

def withdraw():
    myInput2 = int(myInput_num.get())
    myWith = myDepo - myInput2
    myLbl_withdraw.config(text=myWith, bg="#ffffff", width=10, font=("Helvetica", 14, "bold"), fg="#4F091D")
    myLbl_withdraw.grid(row=3, column=2, padx=23)
    
    myInput_num.delete(0, END)

def exit():
    quit("Thank You For Visting My ATM")

myLbl_txt = Label(root, bg="#97BFB4")
myLbl_txt.grid(row=0, column=0)

myInput_num = Entry(root, width=20, bd=2, highlightthickness=1, font=("Helvetica", 14, "bold"))
myInput_num.grid(row=1, column=0, padx=10, pady= 10, ipady=5, sticky=W)
myInput_num.get()

myLbl_wel = Label(root, bg="#97BFB4")
myBtn_wel = Button(root, text="Enter Your Pin Code", font=("Helvetica", 14, "bold"), command=pin, width=18, bg="#F5EEDC")
myBtn_wel.grid(row=2, column=0, padx=10, sticky=W)

myLbl_curbal = Label(root, bg="#97BFB4")
myLbl_curbal.grid()

myFrm_curbal = Label(root, bg="#97BFB4")
myFrm_curbal.grid()

myLbl_initbal = Label(root)
myBtn_initbal = Button(root, text="Set Initial Balance", font=("Helvetica", 14, "bold"), command=initbal, width=18, bg="#F5EEDC", state=DISABLED)
myBtn_initbal.grid(row=3, column=0, padx=10, pady= 5, sticky=W)

myLbl_rembal = Label(root)
myBtn_rembal = Button(root, text="Remaining Balance", font=("Helvetica", 14, "bold"), width=18, command=rembal, bg="#F5EEDC", state=DISABLED)
myBtn_rembal.grid(row=4, column=0, padx=10, sticky=W)

myLbl_deposit = Label(root)
myBtn_deposit = Button(root, text="Deposit", font=("Helvetica", 14, "bold"), width=18, command=deposit, bg="#F5EEDC", state=DISABLED)
myBtn_deposit.grid(row=5, column=0, padx=10, pady= 5, sticky=W)

myLbl_withdraw = Label(root)
myBtn_withdraw = Button(root, text="Withdraw", font=("Helvetica", 14, "bold"), width=18, command=withdraw, bg="#F5EEDC", state=DISABLED)
myBtn_withdraw.grid(row=6, column=0, padx=10, sticky=W)

myLbl_exit = Label(root)
myBtn_exit = Button(root, text="Exit", font=("Helvetica", 14, "bold"), width=18, bg="#F05454", command=exit)
myBtn_exit.grid(row=7, column=0, padx=10, pady= 5, sticky=W)

myLbl_name = Label(root, text="Submitted By: Christian R. Macatangay", font=("Helvetica", 8, "bold"), bg="#97BFB4")
myLbl_name.grid(row=8, column=0, padx=10, pady= 10, sticky=W)

root.mainloop()
