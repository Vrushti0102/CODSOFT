from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#703642')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Devin', 'Patel', '8967859406', 'Melay Street'],
    ['Gaurav', 'Patil', '5211552228', 'Rabey Street'],
    ['Abhishek', 'Nikam', '7894561498', 'India Street'],
    ['Sakshi', 'Gaikwad', '5874524676', 'Coho Street'],
    ['Mohit', 'Paul', '5846975546', 'Nica Street'],
    ['Karan', 'Patel', '5647892989', 'Mine Street'],
    ['Sam', 'Sharma', '8968532067', 'Tibica street'],
    ['John', 'Maheshwari', '9856478545', 'Volvo Street'],
    ['Ganesh', 'Pawar', '8596741222', 'Osian Street'],

]

FirstName = StringVar()
LastName = StringVar()
Phone = StringVar()
Address = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

# Defining the top
Label(root, text='WELCOME TO CONTACT BOOK!!', font=("Cambria", 20)).place(x=170, y=10)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('cambria', 16), bg="#efdecd", width=55, height=10, borderwidth=5, relief="raised")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=TOP, fill=BOTH, expand=1)

def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

def AddContact():
    if FirstName.get() != "" and LastName.get() != "" and Phone.get() != "" and Address.get() != "":
        contactlist.append([FirstName.get(), LastName.get(), Phone.get(), Address.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact.")
    else:
        messagebox.showerror("Error", "Please fill in all the information.")

def UpdateDetail():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    elif FirstName.get() != "" and LastName.get() != "" and Phone.get() != "" and Address.get() != "":
        contactlist[Selected()] = [FirstName.get(), LastName.get(), Phone.get(), Address.get()]
        messagebox.showinfo("Confirmation", "Successfully Updated the Contact.")
        EntryReset()
        Select_set()
    else:
        messagebox.showerror("Error", "Please fill in all the information.")

def EntryReset():
    FirstName.set('')
    LastName.set('')
    Phone.set('')
    Address.set('')

def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'Are you sure you want to delete the selected contact?')
        if result == True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the contact.')

def VIEW():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        FIRSTNAME, LASTNAME, PHONE, ADDRESS = contactlist[Selected()]
        FirstName.set(FIRSTNAME)
        LastName.set(LASTNAME)
        Phone.set(PHONE)
        Address.set(ADDRESS)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for contact in contactlist:
        select.insert(END, f"{contact[0]} {contact[1]} - {contact[2]}")

Select_set()

Label(root, text='First Name:', font=("Cambria", 14)).place(x=30, y=60)
Entry(root, textvariable=FirstName, width=35).place(x=140, y=65)
Label(root, text='Last Name:', font=("Cambria", 14)).place(x=30, y=95)
Entry(root, textvariable=LastName, width=35).place(x=140, y=98)
Label(root, text='Phone No.:', font=("Cambria", 14)).place(x=370, y=60)
Entry(root, textvariable=Phone, width=35).place(x=470, y=98)
Label(root, text='Address:', font=("Cambria", 14)).place(x=370, y=95)
Entry(root, textvariable=Address, width=35).place(x=470, y=64)

Button(root, text="Add Contact", font='Cambria', command=AddContact).place(x=30, y=430)
Button(root, text="Edit Contact", font='Cambria', command=UpdateDetail).place(x=160, y=430)
Button(root, text="Delete Contact", font='Cambria', command=Delete_Entry).place(x=290, y=430)
Button(root, text="View Contact", font='Cambria', command=VIEW).place(x=440, y=430)
Button(root, text="Reset", font='Cambria', command=EntryReset).place(x=580, y=430)
Button(root, text="Exit", font='Cambria', bg='#efdecd', command=EXIT, padx=10).place(x=310, y=490)

root.mainloop()
