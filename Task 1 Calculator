"""
Dimensions of Buttons -
    height: 1
    width: 3 (or (height*2)+1)
Distance between two buttons -
    In Rows: 60
    In Columns: 60

Font size in buttons: 9
"""
# Importing everything from tkinter
from tkinter import *
from tkinter.messagebox import showerror

# Creating the functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')


# Creating a GUI
root = Tk()
root.title("CALCULATOR")
root.geometry('1000x600')
root.resizable(0, 0)
root.configure(background='Lightblue')

# StringVar variables
entry_strvar = StringVar(root)

# Defining the top
Label(root, text='MINI CALCULATOR', font=("Candara", 24), fg='Dark blue' ).place(x=370, y=20)

Label(root, text='Press \'x\' twice for exponentiation', font=("Candara", 10), fg='Dark blue' ).place(x=403, y=70)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=20, font=('arial',18, 'bold'), bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2,state='disabled')
eqn_entry.place(x=370, y=104)

# Number Buttons
Button(root, height=2, width=5, text='8', font=9, bg='White', command=lambda: add_text('7', entry_strvar)).place(x=370, y=206)

Button(root, height=2, width=5, text='8', font=9, bg='White', command=lambda: add_text('8', entry_strvar)).place(x=437, y=206)

Button(root, height=2, width=5, text='9', font=9, bg='White', command=lambda: add_text('9', entry_strvar)).place(x=504, y=206)

Button(root, height=2, width=5, text='4', font=9, bg='White', command=lambda: add_text('4', entry_strvar)).place(x=370, y=272)

Button(root, height=2, width=5, text='5', font=9, bg='White', command=lambda: add_text('5', entry_strvar)).place(x=437, y=272)

Button(root, height=2, width=5, text='6', font=9, bg='White', command=lambda: add_text('6', entry_strvar)).place(x=504, y=272)

Button(root, height=2, width=5, text='1', font=9, bg='White', command=lambda: add_text('1', entry_strvar)).place(x=370, y=338)

Button(root, height=2, width=5, text='2', font=9, bg='White', command=lambda: add_text('2', entry_strvar)).place(x=437, y=338)

Button(root, height=2, width=5, text='3', font=9, bg='White', command=lambda: add_text('3', entry_strvar)).place(x=504, y=338)

Button(root, height=2, width=5, text='0', font=9, bg='White', command=lambda: add_text('0', entry_strvar)).place(x=370, y=404)

# Operator Buttons
add = Button(root, height=2, width=5, text='+', font=9, bg='LightGrey', command=lambda: add_text('+', entry_strvar))
add.place(x=571, y=404)

subtract = Button(root, height=2, width=5, text='-', font=9, bg='LightGrey', command=lambda: add_text('-', entry_strvar))
subtract.place(x=571, y=338)

multiply = Button(root, height=2, width=5, text='x', font=9, bg='LightGrey', command=lambda: add_text('*', entry_strvar))
multiply.place(x=571, y=272)

divide = Button(root, height=2, width=5, text='/', bg='LightGrey', font=9, command=lambda: add_text('/', entry_strvar))
divide.place(x=571, y=206)

decimal = Button(root, height=2, width=5, text='.', font=9, bg='LightGrey', command=lambda: add_text('.', entry_strvar))
decimal.place(x=437, y=404)

bracket_open = Button(root, height=2, width=5, text='(', font=9, bg='LightGrey', command=lambda: add_text('(', entry_strvar))
bracket_open.place(x=437, y=140)

bracket_close = Button(root, height=2, width=5, text=')', font=9, bg='LightGrey', command=lambda: add_text(')', entry_strvar))
bracket_close.place(x=503, y=140)

# Equal, C and AC buttons
equal = Button(root, height=2, width=5, text='=', font=9, bg='Teal', command=lambda: submit(eqn_entry, entry_strvar))
equal.place(x=504, y=404)

clear = Button(root, height=2, width=5, text='C', font=9, bg='Teal',
               command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))
clear.place(x=570, y=140)

AC_btn = Button(root, height=2, width=5, text='AC', font=9, bg='Teal', command=lambda: entry_strvar.set(''))
AC_btn.place(x=371, y=140)

# Ok Button
ok_btn = Button(root, height=2, width=23, text='OK', font=9, bg='Teal', command=lambda: root.destroy())
ok_btn.place(x=371, y=470)

# Updating root
root.update()
root.mainloop()
