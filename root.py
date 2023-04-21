# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

# MAIN_IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

# Create_Test_Frame
def test_on():
    tests_main_frame.tkraise()

# Create_NoteBook_Frame
def notebook_on():
    notebook_main_frame.tkraise()

# Create_Table_Frame
def table_on():
    table_main_frame.tkraise()

# Main_Root_Settings
root = tkb.Window(themename="vapor")
root.geometry("1000x500+300+200")
root.resizable(False, False)
root.title("Mentala")

# Functions
def save_content():
    content = my_text.get("1.0", "end-1c")
    with open("saved_content.txt", "w") as f:
        f.write(content)

# App Menu
main_menu = tkb.Menu(root)
root.config(menu=main_menu)

# Menu Items
file_menu = tkb.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="Save", command=save_content)

# Root_Grid_Configure
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

# ------Menu_Frame------
menu_frame = tkb.Frame(root)
menu_frame.grid(row=0, column=0, sticky="nsew")
# Menu Label
menu_label = tkb.Label(menu_frame, text="ГОЛОВНЕ МЕНЮ", font=("Gotham-bold", 15), bootstyle="primary")
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
# Version_Label
version_label = tkb.Label(menu_frame, text="Mentala Beta 2023 | 0.3", font=("Gotham", 10), bootstyle="primary")
version_label.pack(anchor="sw", side=tkb.BOTTOM, padx=10)
# ------Menu_Frame------

# ==========Create NoteBook_Widget=========
notebook_main_frame = tkb.Frame(root, bootstyle="dark")
notebook_main_frame.grid(row=0, column=1, sticky="nsew")
# Test_Frame_Name
test_name_label = tkb.Label(notebook_main_frame, text="НОТАТКИ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
test_name_label.pack(pady=10)
my_notebook = tkb.Notebook(notebook_main_frame, bootstyle='dark')
my_notebook.pack(pady=20)
# Create PAGE
tab1 = tkb.Frame(my_notebook)
# Create TextField
my_text = tkb.Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)
# Add Frame
my_notebook.add(tab1, text='NOTES')
# ==========Create NoteBook_Widget=========

# ==========Tests_Frame=========
tests_main_frame = tkb.Frame(root, bootstyle="dark")
tests_main_frame.grid(row=0, column=1, sticky="nsew")
# Test_Frame_Name
test_name_label = tkb.Label(tests_main_frame, text="ТЕСТУВАННЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
test_name_label.pack(pady=10)
# ==========Tests_Frame=========

# ==========Table_Frame=========
table_main_frame = tkb.Frame(root, bootstyle="dark")
table_main_frame.grid(row=0, column=1, sticky="nsew")
# Test_Frame_Name
test_name_label = tkb.Label(table_main_frame, text="ТАБЛИЦЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
test_name_label.pack(pady=10)
# ==========Table_Frame=========

# Set_Default_Frame
tests_main_frame.tkraise()
# Execute_Main_Loop
root.mainloop()

