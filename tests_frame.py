# Фрейм для тестів (20.04.2023)
# IMPORTS
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

def create_test_frame(root):
    # ------Tests_Frame------
    tests_main_frame = tkb.Frame(root, bootstyle="dark")
    tests_main_frame.grid(row=0, column=1, sticky="nsew")
    # Test_Frame_Name
    test_name_label = tkb.Label(tests_main_frame, text="ТЕСТУВАННЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
    test_name_label.pack(pady=10)
    # ------Tests_Frame------