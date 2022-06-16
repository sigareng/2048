import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class App(tk.Tk):
    def __init__(self, *args, **kwargs) :
        super().__init__()

        self.title('Login')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def quit(self):
        self.quit()        
    def create_widgets(self):
        # username
        f = ('Times', 14)
        username_label = ttk.Label(self,text="Username",font=f)
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:",font=f)
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self,width=15, text='Login', command=lambda: App.login(username_entry.get(),password_entry.get()))
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    def login(user,passwd):
        try:
            con = sqlite3.connect('data.db')
            c = con.cursor()
            for row in c.execute("Select * from users"):
                username = row[0]
                pwd = row[1]
            # username = 'asa'
            # pwd = 'kata'
            
        except Exception as ep:
            messagebox.showerror('', ep)

        uname = user
        upwd = passwd
        check_counter=0
        if uname == "":
           warn = "Username can't be empty"
        else:
            check_counter += 1
        if upwd == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
                # self.destroy()
                App.quit()
                print(username)
                print(dir())
                play.GameGrid()
            else:
                messagebox.showerror('Login Status', 'invalid username or password')
        else:
            messagebox.showerror('', warn)

if __name__ == "__main__":
    app = App()
    app.mainloop()