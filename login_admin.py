import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
login_app=ttk.Tk()
login_app.title('Login')
login_app.geometry('600x400')
font_=font.Font(size=20)

uname= ttk.Variable(login_app)
pwd= ttk.Variable(login_app)

ttk.Label(
    login_app,
    text='Enter your credentials', 
    font=font_
).place(x=200,y=20)
ttk.Label(login_app,text='Username').place(x=100,y=80)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=250,y=80)

ttk.Label(login_app,text='Password').place(x=100,y=130)
ttk.Entry(login_app,font=font_,show='*',textvariable=pwd).place(x=250,y=130)

def submit():
    op=''
    with open('opr','r')as f:
        op = f.read()
    if len(op)> 0:
        userid=uname.get()
        passward=pwd.get()
        p=open('pwd').read()
        uname.set('')
        pwd.set('')
        if userid == 'admin' and passward == p:
            print('login succesfull')
            mb.showinfo('Success','Login Succesful')

            if op =='register':
                from tkinter.simpledialog import askstring
                name = askstring('Name','For whom you want to register')
                import register_face as rf
                rf.register(name)
            elif op == 'clear':
                print('clear data')
                import clear_data
                
        else:
            print('login failed')
            mb.showinfo('Error','Login Failed')

def back():
    login_app.destroy()
    with open('opr','w')as f:
        op = f.write('')
    import app

    
ttk.Button(
    login_app,text='Submit',font=font_,command=submit,
    height=1,width=10,bg="#F39C12",    
    ).place(x=250,y=220)

ttk.Button(
    login_app,text='Back',font=font_,command=back,
    height=1,width=6,    
    ).place(x=20,y=340)


login_app.mainloop()