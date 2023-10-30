from tkinter import *
root = Tk ()

root.geometry ('400x400')

root.config (bg= 'slateGray3')
root.resizable(0,0)
root.title('Contact Book')

contactlist = []

Name = StringVar()

Number = StringVar()

Email = StringVar()

Address = StringVar()

frame = Frame(root)

frame.pack(side = RIGHT)

Scroll = Scrollbar (frame, orient = VERTICAL)
select = Listbox (frame,yscrollcommand = Scroll.set, height = 12)

Scroll.config(command = select.yview)
Scroll.pack (side = RIGHT, fill = Y)


select.pack (side = LEFT, fill = BOTH, expand = 1)

def Selected():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
    Select_set()

def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Email.get(),Address.get() ]
    Select_set()

def DELETE():
    del contactlist[Selected()]
    Select_set()

def VIEW():
    NAME,NUMBER,EMAIL,ADDRESS = contactlist[Selected()]

    Name.set(NAME)

    Number.set(NUMBER)
    Email.set(EMAIL)
    Address.set(ADDRESS)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, email, address in contactlist:

        select.insert (END, name)

Select_set()

Label(root, text = 'NAME', font = 'arial 12 bold', bg= 'SlateGray3').place ( x = 30 ,y = 20 )

Entry(root, textvariable = Name).place ( x = 100, y = 20 )

Label(root, text = "PHONE NO:",font = 'arial 12 bold', bg= 'SlateGray3').place (x=30, y=70)
Entry(root, textvariable = Number).place(x = 130 ,y = 70 )

Label(root, text = "EMAIL:",font = 'arial 12 bold', bg= 'SlateGray3').place (x=30, y=120)
Entry(root, textvariable = Email).place(x = 130 ,y = 120 )

Label(root, text = "ADDRESS:",font = 'arial 12 bold', bg= 'SlateGray3').place(x=30, y=170)
Entry(root, textvariable = Address).place(x = 130 ,y = 170 )



Button(root, text="ADD", font = 'arial 12 bold', bg= 'SlateGray4', command = AddContact).place(x= 100, y=210)

Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4', command = DELETE).place(x= 100, y=260)
Button(root, text="VIEW", font='arial 12 bold', bg="SlateGray4", command = VIEW).place(x= 100, y=310)

Button(root, text="EXIT", font="arial 12 bold", bg= 'tomato', command = EXIT).place(x= 300, y=320)
#Button(root, text="RESET", font='arial 12 bold', bg="SlateGray4", command = RESET).place(x= 50, y=310)
root.mainloop()
