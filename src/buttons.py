from tkinter import Tk
from tkinter import Label
from tkinter import Button
from testingView import startPage
from cabinetView import startCabinet

root = Tk()
root.geometry('420x300')
root.title("MedHelper")
#root.config(background="white")

def exitt():
    exit()
    
def testing_window():
    startPage()

def cabinet_window():
    startCabinet()

 
label_0 = Label(root, text="MedHelper",relief="solid",width=20,fg='brown', font=("comis sans ms", 15,"bold"))
label_0.place(x=80,y=40)

but_cabinet=Button(root, text='Open Cabinet View',width=20,bg='brown',fg='white',command=cabinet_window).place(x=30,y=120)
but_testing=Button(root, text='Open Testing View',width=20,bg='brown',fg='white',command=testing_window).place(x=240,y=120)
but_quit=Button(root,text="Quit",width=12,bg='brown',fg='white',command=exitt).place(x=160,y=200)

root.mainloop()