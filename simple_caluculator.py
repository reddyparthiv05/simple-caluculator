import tkinter as tk
def addition():
    num1=int(Entry1.get())
    num2=int(Entry2.get())
    sum=num1+num2
    label3.config(text=sum)
def subtraction():
    num1=int(Entry1.get())
    num2=int(Entry2.get())
    difference=num1-num2
    label3.config(text=difference)
def multiplication():
    num1=int(Entry1.get())
    num2=int(Entry2.get())
    product=num1*num2
    label3.config(text=product)
def division():
    num1=int(Entry1.get())
    num2=int(Entry2.get())
    division=num1/num2
    label3.config(text=division) 
def ac():
    Entry1.delete(0,tk.END)   
    Entry2.delete(0,tk.END)
    label3.config(text='')
root=tk.Tk()
root.title('simple caluculator')
root.geometry('1000x1000')
root.config(bg='lightblue')
label1=tk.Label(root,text='ENTER THE FIRST NUMBER',bg='blue',fg='white',font='Helvetica 16 bold')
label1.place(x=300,y=100)
Entry1=tk.Entry(root)
Entry1.place(x=300,y=150)
label2=tk.Label(root,text='ENTER THE SECOND NUMBER',bg='blue',fg='white',font='Helvetica 16 bold')
label2.place(x=300,y=250)
Entry2=tk.Entry(root)
Entry2.place(x=300,y=300)
button1=tk.Button(root,text='CALUCULATE THE SUM',command=addition,bg='lightblue',fg='black')
button1.place(x=300,y=400)
button2=tk.Button(root,text='CALUCULATE THE DIFFERENCE',command=subtraction,bg='lightblue',fg='black')
button2.place(x=300,y=500)
button3=tk.Button(root,text='CALUCULATE THE PRODUCT',command=multiplication,bg='lightblue',fg='black')
button3.place(x=300,y=600)
button4=tk.Button(root,text='CALUCULATE THE DIVISION',command=division,bg='lightblue',fg='black')
button4.place(x=300,y=700)
button5=tk.Button(root,text='AC',command=ac)
button5.place(x=300,y=750)
label3=tk.Label(root,text='')
label3.place(x=300,y=800)
root.mainloop()