# -*- coding: utf-8 -*- # за каким-то хреном он тупой, и не понимает, что тут UTF-8
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *


# Settings
root = tkb.Window(themename="vapor", resizable=(False, False))
root.geometry("500x500+300+200")

my_login = "sasha"
my_password = "kior"

def check_on():
    global my_login, my_password
    if login_entry.get() == my_login and password_entry.get() == my_password:
        login_entry.config(bootstyle='success')
        password_entry.config(bootstyle='success')
    else:
        login_entry.config(bootstyle='danger')
        password_entry.config(bootstyle='danger')


# Main_Frame_Section
main_frame_entry = tkb.Frame(root, bootstyle="dark", padding=(20, 10))
main_frame_entry.pack(expand=TRUE)

# Meetings Section
mentala_label = tkb.Label(main_frame_entry, text='MENTALA', bootstyle="inverse-dark", font=("Gotham-bold", 20))
mentala_label.grid(row=0, column=0, columnspan=3, pady=5)

# Login_Section
login_label = tkb.Label(main_frame_entry, text='Login: ', bootstyle="inverse-dark", font=("Gotham-bold", 10))
login_label.grid(row=1, column=0, padx=10, pady=10)
login_entry = tkb.Entry(main_frame_entry, width=20, show="*")
login_entry.grid(row=1, column=1, padx=10, pady=10)

# Password Section
password_label = tkb.Label(main_frame_entry, text='Password: ', bootstyle="inverse-dark", font=("Gotham-bold", 10))
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tkb.Entry(main_frame_entry, width=20, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Accept Section
accept_button = tkb.Button(main_frame_entry, text="ПРИНЯТЬ", bootstyle="primary-outline", command=check_on)
accept_button.grid(row=3, column=0, columnspan=3, pady=5)
# Execute
root.mainloop()
