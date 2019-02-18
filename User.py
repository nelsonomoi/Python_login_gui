import tkinter as tk
from database_con import save_new_user
window=tk.Tk()

window.title("Registration")
window.geometry('600x400')

def register_user():
    username=str(userEntry.get())
    password=str(passEntry.get())
    try:
        if username!='' and password!='':
            save_new_user(username,password)
            window.destroy()

        else:
            print('Username or password must not be empty')

    except:
        print('Failed')



userLabel=tk.Label(text='Username')
userLabel.grid(column=3,row=3,ipady=2,ipadx=2,pady=50,padx=80)

passLabel=tk.Label(text='Password')
passLabel.grid(column=3,row=4,ipady=2,ipadx=2)

userEntry=tk.Entry(width=20)
userEntry.grid(column=4,row=3,padx=4,ipady=4,ipadx=4)

passEntry=tk.Entry(width=20)
passEntry.grid(column=4,row=4,padx=4,ipady=4,ipadx=4)

loginbtn=tk.Button(text='Register',command=register_user)
loginbtn.grid(column=4,row=6,ipady=2,padx=20,pady=30)

window.mainloop()