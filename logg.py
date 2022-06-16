import tkinter
import puzzle as play

from tkinter import *

class LoginForm(Frame):
 def __init__(self,master=None):
    super().__init__(master)
    self.pack()
    self.createWidget()

 def createWidget(self):
    self.lblEmailId=Label(self,text="Email Id")
    self.lblEmailId.grid(row=0,column=0)
    self.varEmailid=StringVar()
    self.txtEmailId=Entry(self,textvariable=self.varEmailid)
    self.txtEmailId.grid(row=0,column=1)
    self.txtEmailId.bind("<KeyRelease>",self.key_press)

    self.lblPassword = Label(self, text="Password")
    self.lblPassword.grid(row=1, column=0)
    self.varPassword=StringVar()

    self.txtPassword= Entry(self, textvariable=self.varPassword)
    self.txtPassword.grid(row=1, column=1)
    self.btnLogin=Button(self,text="Login")
    self.btnLogin.grid(row=2,column=1)
    self.btnLogin.bind("<Button-1>",self.btnLogin_click)

 def btnLogin_click(self,event):
    self.varPassword.set(self.varEmailid.get())
    # LoginWindow=Toplevel()
    play.GameGrid()






 def key_press(self,event):
    self.varPassword.set(self.varEmailid.get())


root=Tk()
fromLogin=LoginForm(root)
root.mainloop()