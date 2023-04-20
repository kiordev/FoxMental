# Фрейм для таблиці СМЄР (20.04.2023)
# IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

def create_table_frame(root):
    # ------Table_Frame------
    table_main_frame = tkb.Frame(root, bootstyle="dark")
    table_main_frame.grid(row=0, column=1, sticky="nsew")
    # Test_Frame_Name
    test_name_label = tkb.Label(table_main_frame, text="ТАБЛИЦЯ", font=("Gotham-bold", 15),bootstyle="inverse-dark")
    test_name_label.pack(pady=10)
    # ------Table_Frame------