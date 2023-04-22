# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

# MAIN_IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *
import NoteBookFrame as ntf
import TestsFrame as tf
import TableFrame as tabf

# On_Test_Frame
def test_on():
    tf.TestsFrameOn(root)

# On_NoteBook_Frame
def notebook_on():
    ntf.NoteBookOn(root)

# On_Table_Frame
def table_on():
    tabf.TableFrameOn(root)


# Accept Theme
def accept_theme():
    root.style.theme_use(themename=my_theme[theme_combobox.current()])

# Main_Root_Settings
root = tkb.Window(themename="vapor")
root.geometry("1000x500+300+200")
root.resizable(False, False)
root.title("Mentala")

# Functions

# Root_Grid_Configure
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

# ------Menu_Frame------
menu_frame = tkb.Frame(root)
menu_frame.grid(row=0, column=0, sticky="nsew")

# Menu Label
menu_label = tkb.Label(menu_frame, text="ГОЛОВНЕ МЕНЮ", font=("Gotham-bold", 10), bootstyle="primary")
menu_label.pack(pady=10)

# Start_Test_Button
test_button = tkb.Button(menu_frame, text='ПРОЙТИ ТЕСТ', bootstyle="primary", width=20, command=test_on)
test_button.pack(pady=10)

# Start_Table_Button
table_button = tkb.Button(menu_frame, text='ТАБЛИЦЯ', bootstyle="primary", width=20, command=table_on)
table_button.pack(pady=10)

# Start_NoteBook_Button
notebook_button = tkb.Button(menu_frame, text='НОТАТКИ', bootstyle="primary", width=20, command=notebook_on)
notebook_button.pack(pady=10)

# Separator
menu_separator = tkb.Separator(menu_frame, bootstyle='primary')
menu_separator.pack(fill='x', pady=10)

# Settings Label
settings_label = tkb.Label(menu_frame, text="НАЛАШТУВАННЯ", font=("Gotham-bold", 10), bootstyle="primary")
settings_label.pack(pady=10)

# Theme Combo Box
my_theme = root.style.theme_names()
theme_combobox = tkb.Combobox(menu_frame, values=my_theme)
theme_combobox.pack(pady=5, padx=10)
accept_theme_button = tkb.Button(menu_frame, bootstyle='primary', text='ACCEPT THEME', command=accept_theme)
accept_theme_button.pack(pady=10, padx=10)
theme_combobox.current(15)

# Version_Label
version_label = tkb.Label(menu_frame, text="Mentala | 0.5 | WINDOWS", font=("Gotham", 10), bootstyle="primary")
version_label.pack(anchor="s", side=tkb.BOTTOM, padx=10)

# ------Menu_Frame------

# Set_Default_Frame
tf.TestsFrameOn(root)

# Execute_Main_Loop
root.mainloop()

