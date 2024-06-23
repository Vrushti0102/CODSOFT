import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("To Do List")
root.geometry("500x600+600+200")
root.resizable(False,False)
v=tk.BooleanVar()
ck=tk.Checkbutton(root,)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
         task_list.remove(task)
         with open("tasklist.txt",'w') as taskfile:
             for task in task_list:
                 taskfile.write(task+"\n")
         listbox.delete(ANCHOR)

def complete_task():
        try:
            selected_task_index = task_list.curselection()[0]
            task_list.itemconfig(selected_task_index, {'bg': 'light grey'})
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file=open('tasklist.txt','w')
        file.close()

#Create a canvas
canvas= Canvas(root, width=600, height=400)
canvas.pack()

#icon
Image_icon=PhotoImage(file="list.png")
root.iconphoto(False,Image_icon)

#topbar
TopImage=PhotoImage(file="image.png")
Label(root,image=TopImage).place(x=10,y=1)
Label(root, text='~ TO DO List ~', font=("Monotype Corsiva", 28)).place(x=152, y=40)
Label(root, text='Reminds me Everything', font=("Bradley Hand ITC", 12, "italic")).place(x=171, y=100)

#menu
img=(Image.open("menu.png"))

resized_image= img.resize((20,10))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

#main
frame= Frame(root,width=295,height=45, bg="#2F5061")
frame.place(x=14,y=210)
task=StringVar()
task_entry=Entry(frame,width=25,font="Cambria 14",bd=3)
task_entry.place(x=5,y=7)
task_entry.focus()

#add button
button1=Button(text="Add Task",font="Cambria 11",width=20,height=2,bg="#4297A0",bd=1,command=addTask)
button1.place(x=330,y=210)

#mark as complete
complete_task_button = tk.Button(root, text="Mark as Completed",width=23,height=2,bg="#4297A0", bd=1, command=complete_task)
complete_task_button.place(x=330,y=260)


#listbox
frame1= Frame(root,bd=2,width=200,height=100,bg="#2F5061")
frame1.pack(pady=(20,70))
frame1.place(x=13,y=260)

listbox= Listbox(frame1,font=('Cambria',18), width=21,height=10,bg="#2F5061",fg="White", cursor="hand2",selectbackground="#2F5061")
listbox.pack(side=LEFT , fill=BOTH, padx=2)

Scrollbar=Scrollbar(frame1)
Scrollbar.pack(side= RIGHT ,fill= BOTH)
listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
image = Image.open("delete.png")
image = image.resize((30, 30))
photo = ImageTk.PhotoImage(image)
button2 = tk.Button(root,image=photo, command=deleteTask).place(x=330,y=310)
Label(root, text="Delete the task",bg="#4297A0",width=17,height=2).place(x=370,y=310)

root.mainloop()

