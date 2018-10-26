from tkinter import *
import detail_back
window = Tk()

s1=Scrollbar(window)
lis= Listbox(window,yscrollcommdand=s1.set(2,8))
lis.grid(row= 8,column=2)

s1.grid(row=8,column=3)
s1.config(command=lis.yview())


def get_selected(event):
    global e11
    index= lis.curselection()[0]
    e11=lis.get(index)


def sel():
    clr()
    e1.insert(END, e11[0])
    e2.insert(END,e11[1])
    e3.insert(END, e11[2])
    e4.insert(END, e11[3])


def upda():
    detail_back.update(e1.get(),e2.get(),e3.get(),e4.get())
    clr()

def search():
    j=detail_back.search(e3.get())
    lis.delete(0,END)
    lis.insert(END,j)
    clr()

def adda():
    detail_back.add(e1.get(),e2.get(),e3.get(),e4.get())
    clr()

def view1():
    lis.delete(0,END)
    for i in detail_back.view():
        lis.insert(END,i)
    clr()



def dele():
    detail_back.delete(e3.get())
    clr()

def clr():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0,END)
    e4.delete(0,END)


l1=Label(window, text="Name")
l1.grid(row=0,column=0)

l2=Label(window, text="Contact")
l2.grid(row=0,column=4)

l3=Label(window, text="ID No.")
l3.grid(row=3,column=0)

l4=Label(window, text="Salary")
l4.grid(row=3,column=4)

name_text= StringVar()
e1= Entry(window, textvariable=name_text)
e1.grid(row= 0,column= 1)

contact_text= IntVar()
e2= Entry(window, textvariable=contact_text )
e2.grid(row= 0,column= 5)

idn_text= IntVar()
e3= Entry(window, textvariable=idn_text)
e3.grid(row= 3,column= 1)

sal_text= IntVar()
e4= Entry(window, textvariable=sal_text)
e4.grid(row= 3,column= 5)

b1=Button(window,text="Add",command=adda)
b1.grid(row=5,column=0)

b2=Button(window,text="Delete",command=dele)
b2.grid(row=5,column=2)

b3=Button(window,text="Search",command=search)
b3.grid(row=5,column=1)

b4=Button(window,text="Update",command=upda)
b4.grid(row=5,column=5)

b5=Button(window,text="View", command=view1)
b5.grid(row=6,column=2)

b6=Button(window,text="Select", command=sel)
b6.grid(row=8,column=0)

lis.bind('<<ListboxSelect>>',get_selected)

window.mainloop()