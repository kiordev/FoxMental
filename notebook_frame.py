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
    test_name_label = tkb.Label(notebook_main_frame, text="ТЕСТУВАННЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
    test_name_label.pack(pady=10)
    # ------NoteBook_Frame------