# Фрейм для записів (20.04.2023)

# IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

def create_notebook_frame(root):
    # ------NoteBook_Frame------
    notebook_main_frame = tkb.Frame(root, bootstyle="dark")
    notebook_main_frame.grid(row=0, column=1, sticky="nsew")
    # Test_Frame_Name
    test_name_label = tkb.Label(notebook_main_frame, text="НОТАТКИ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
    test_name_label.pack(pady=10)

    # Create NoteBook_Widget
    my_notebook = tkb.Notebook(notebook_main_frame, bootstyle='dark')
    my_notebook.pack(pady=20)

    # Create PAGE
    tab1 = tkb.Frame(my_notebook)

    # Create TextField
    my_text = tkb.Text(tab1, width=70, height=10)
    my_text.pack(pady=10, padx=10)

    # Add Frame
    my_notebook.add(tab1, text='NOTES')

    # ------NoteBook_Frame------