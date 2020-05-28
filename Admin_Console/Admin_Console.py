import tkinter as tk
from tkinter import messagebox
import json
import os
import sys
import time
path = os.getcwd()
root = tk.Tk()
root.title('Login')
root.iconbitmap(r'AnyConv.com__password.ico')
with  open(path + '\Data.json','r') as data:
    Loaded = json.load(data)
def create_window():
    Mainwindow = tk.Tk()
    Mainwindow.title('Admin_console')
    Mainwindow.iconbitmap(r'AnyConv.com__user.ico')
    def shut():
        os.system('shutdown /s /t 1')
    tk.Button(Mainwindow,command=shut, text='shutdown pc',fg='red',width = 15,height=5).grid(row=2,column=0)
    def Reset():
        with  open(path + '\Data.json','w') as data:
                data.write(json.dumps({
                    "UserName":None,
                    "Password":None,
                    "NewUser":True,
                    "Locked":True
                }))
        messagebox.showinfo('account reset','your account has been reset succesfully')
        Mainwindow.destroy()      
    tk.Button(Mainwindow,command=Reset, text='Reset Account',fg='red',width = 15,height=5).grid(row=0,column=0)
    def Rename():
        newusername = tk.StringVar(Mainwindow)
        window = tk.Toplevel(Mainwindow)
        def click():    
            with  open(path + '\Data.json','w') as data:
                if not newusername.get() == None:
                    data.write(json.dumps({
                        "UserName":newusername.get(),
                        "Password":loaded["Password"],
                        "NewUser":False,
                        "Locked":loaded["Locked"]
                    }))
                    messagebox.showinfo('username','Your username has been changed')
                    Mainwindow.destroy()

                else:
                    messagebox.showerror('Error',"Your Username can't be empty")    
        tk.Button(window, command=click,text='Change username',).grid(row=1,column=1)
        tk.Entry(window, textvariable=newusername,).grid(row=0,column=1)
        tk.Label(window,text='New username:').grid(row=0,column=0)
    def restart():
        os.system('shutdown /r /t 1')
    tk.Button(Mainwindow,command=restart, text='restart pc',fg='green',width = 15,height=5).grid(row=4,column=0)
    tk.Button(Mainwindow,command=Rename, text='Change username',width = 15,height=5).grid(row=1,column=0)
    def Repass():
        newpassword = tk.StringVar(Mainwindow)
        oldpassword = tk.StringVar(Mainwindow)
        window = tk.Toplevel(Mainwindow)
        def click():    
            with  open(path + '\Data.json','w') as data:
                if not newpassword.get() == None:
                    if oldpassword.get() == loaded["Password"]:
                        data.write(json.dumps({
                            "UserName":loaded["UserName"],
                            "Password":newpassword.get(),
                            "NewUser":False,
                            "Locked":loaded["Locked"]
                        }))
                        messagebox.showinfo('password','Your password has been changed')
                        Mainwindow.destroy()

                else:
                    messagebox.showerror('Error',"Your Password can't be empty")    
        tk.Button(window, command=click,text='Change password',).grid(row=2,column=1)
        tk.Entry(window, textvariable=oldpassword,).grid(row=1,column=1)
        tk.Entry(window, textvariable=newpassword,).grid(row=0,column=1)
        tk.Label(window,text='Old Password:').grid(row=0,column=0)
        tk.Label(window,text='New Password:').grid(row=1,column=0)
    tk.Button(Mainwindow,command=Repass, text='Change password',width = 15,height=5).grid(row=0,column=1)
    def Lock():
        with  open(path + '\Data.json','w') as data:
            data.write(json.dumps({
                            "UserName":loaded["UserName"],
                            "Password":loaded["Password"],
                            "NewUser":False,
                            "Locked":True
                        }))
            Mainwindow.destroy()
    tk.Button(Mainwindow,command=Lock, text='Lock',width = 15,height=5).grid(row=1,column=1)
    def UnLock():
        with  open(path + '\Data.json','w') as data:
            data.write(json.dumps({
                            "UserName":loaded["UserName"],
                            "Password":loaded["Password"],
                            "NewUser":False,
                            "Locked":False
                        }))
            Mainwindow.destroy()
    tk.Button(Mainwindow,command=UnLock, text='Unlock',width = 15,height=5).grid(row=2,column=1)  
    Mainwindow.mainloop()
with  open(path + '\Data.json','r') as data:
    loaded = json.load(data)
if loaded['NewUser'] == True:
    usernameinput = tk.StringVar()
    passwordinput = tk.StringVar()
    confirmpassword = tk.StringVar()
    tk.Label(root, text='Create new account').grid(row=0,column=1)
    tk.Label(root, text='Username:').grid(row=1,column=1)
    tk.Label(root, text='Password:').grid(row=2,column=1)
    tk.Label(root, text='Confirm Password:').grid(row=3,column=1)
    tk.Entry(root, textvariable = usernameinput,bd=5).grid(row=1,column=2)
    tk.Entry(root,show='*', textvariable = passwordinput,bd=5).grid(row=2,column=2)
    tk.Entry(root,show='*', textvariable = confirmpassword,bd=5).grid(row=3,column=2)
    def logincomm():
        if passwordinput.get() == confirmpassword.get() and not passwordinput.get() == None and not usernameinput.get() == None:
            with  open(path + '\Data.json','w') as data:
                data.write(json.dumps({
                    "UserName":usernameinput.get(),
                    "Password":passwordinput.get(),
                    "NewUser": False,
                    "Locked": True
                }))
            messagebox.showinfo('A new account has been created','Please Restart the application to log in')
            root.destroy()
        else:
            tk.Label(root,fg='red', text="Passwords don't match").grid(row=0,column=0)        
    tk.Button(root,command=logincomm, text='login').grid(row=4,column=2)
else:
    if Loaded["Locked"] == True:
        usernameinput = tk.StringVar()
        passwordinput = tk.StringVar()
        tk.Label(root, text='Username').grid(row=0,column=0)
        tk.Label(root, text='Password').grid(row=2,column=0)
        tk.Entry(root, textvariable = usernameinput,bd=5).grid(row=0,column=1)
        tk.Entry(root,show="*",textvariable = passwordinput,bd=5).grid(row=2,column=1)
        def login():
            if usernameinput.get()== loaded['UserName'] and passwordinput.get() == loaded['Password']:
                print('login succesful')       
                create_window()         
        tk.Button(root, text='Login', command=login).grid(row=3,column =1)  
    else:
        create_window()              
root.mainloop()
