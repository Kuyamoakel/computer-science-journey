import tkinter
from tkinter import messagebox
accounts = [
    {
        "username": "akel",
        "password": "1234"
    },
    {
        "username": "kurt",
        "password": "1234"
    }
]

window = tkinter.Tk()
window.title("Login Form")
window.geometry('500x450')
window.configure(bg='#333333')

def login():
    global accounts
    for acc in accounts:
        if username_entry.get()==acc["username"] and password_entry.get()==acc["password"]:
            messagebox.showinfo(title="Logged", message="You Successfully Logged in")
        else:
            messagebox.showerror(title="Error", message="Invalid Login")

frame = tkinter.Frame(bg='#333333')

# creating widgets
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_entry.grid(row=2, column=1, pady=20)
password_label.grid(row=2, column=0)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop() 