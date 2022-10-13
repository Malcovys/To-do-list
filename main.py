from tkinter import*


root=Tk()#instance
root.title('To-Do-List')#write title
root.geometry('400x650+400+100')#taille de la fen
root.resizable(False,False)#rend la taille de la fenetre modifiable ou pas

task_list=[] #list task list

def addTask():
    task=task_entry.get()#affect la tache dans 'task'
    task_entry.delete(0,END)#libere task_entry pour pouvoir recevoir d'audre task

    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f'\n{task}')#write in 
        task_list.append(task)#affichage
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))

    if task in task_list:
        task_list.remove(task)
        with open('taskList.txt','w') as taskfie:
            for task in task_list:
                taskfie.write(task+'\n')

        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open('tasklist.txt','r') as taskfile:#r pour read
            tasks=taskfile.readlines()#dep les list in task
        
            for task in tasks:#add in list task_list
                if task != '\n':
                    task_list.append(task)
                    listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')#write
        file.close()


#icônes
image_icon=PhotoImage(file='image/icon.png')#instance
root.iconphoto(False,image_icon)

#top bar
TopImage=PhotoImage(file='image/topbar.png')#instance
Label(root,image=TopImage).pack()

"""dockImage=PhotoImage(file='image/dock.png')
Label(root,image=dockImage,bg='#32405b').place(x=30,y=25)
"""
#noteImage=PhotoImage(file='image/Tt.png')
#Label(root,image=noteImage,bg='#32405b').place(x=30,y=25)
#instance
heading=Label(root,text='ALL TASK',font='arial 20 bold',fg='white',bg='#32405b')
heading.place(x=130,y=20)

#paver
frame=Frame(root,width=400,height=50,bg='white')
frame.place(x=0,y=595)

task=StringVar()
task_entry=Entry(frame,width=18,font='arial 20',bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text='ADD',font='arial 20 bold',width=6,bg='#5a95ff',fg='#fff',bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,height=280,bg='white')
#frame1.pack(pady=(0,0))
frame1.place(x=13,y=90)

listbox=Listbox(frame1,font=('arial',12),width=40,height=26,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')

listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file='image/delete.png')
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=(200,80))

root.mainloop()#fait apparaître la fenêtre graphique et la maintien
