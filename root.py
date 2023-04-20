# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

# MAIN_IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *
# APP_IMPORTS
import notebook_frame, tests_frame, table_frame

# Create_Test_Frame
def test_on():
    tests_frame.create_test_frame(root)

# Create_NoteBook_Frame
def notebook_on():
    notebook_frame.create_notebook_frame(root)

# Create_Table_Frame
def table_on():
    table_frame.create_table_frame(root)

# Main_Root_Settings
root = tkb.Window(themename="vapor")
root.geometry("1000x500+300+200")
root.resizable(False, False)
root.title("Mentala")

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
version_label = tkb.Label(menu_frame, text="Mentala Beta 2023 | 0.1", font=("Gotham", 10), bootstyle="primary")
version_label.pack(anchor="sw", side=tkb.BOTTOM, padx=10)
# ------Menu_Frame------

# Set_Default_Frame
tests_frame.create_test_frame(root)
# Execute_Main_Loop
root.mainloop()

