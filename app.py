import tkinter as ttk
from tkinter import font
app=ttk.Tk()
app.title('Attendence System')
app.geometry('600x400')
font_=font.Font(size=20)

ttk.Label(
    app,
    text='Face  Recognition Based Attendence System',
    font=font_
).pack()

def register():
    app.destroy() # destroy first
    with open('opr','w')as f:
        op = f.write('register') 
    import login_admin
    
    

def attendence():
    print('Attendence')
    import attendence
    attendence.attendence()

def clear_data():
    with open('opr','w')as f:
        op = f.write('clear')
    import login_admin
   

ttk.Button(     #fg for font/text color
    app,text='Register',command=register,font=font_,
    height=3,width=15,background="#1ABC9C",
    ).pack(expand=True)

ttk.Button(
    app,text='Attendence',command=attendence,font=font_,
    height=3,width=15,bg="#E67E22",    
    ).pack(expand=True)

ttk.Button(
    app,text='Clear data',command=clear_data,font=font_,    
    height=3,width=15,bg="#3498DB"
    ).pack(expand=True)

app.mainloop()