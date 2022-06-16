import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        f = ('Times', 14)
        username_label = self.Label(self,text="Username",font=f)
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = self.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = self.Label(self, text="Password:",font=f)
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = self.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = self.Button(self,width=15, text='Login', command=lambda: App.login(username_entry.get(),password_entry.get()))
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def login():
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

      uname = email_tf.get()
      upwd = pwd_tf.get()
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
              ws.destroy()
              print(username)
              print(dir())
              play.GameGrid()
          else:
              messagebox.showerror('Login Status', 'invalid username or password')
      else:
          messagebox.showerror('', warn)

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()