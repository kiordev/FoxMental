# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# NoteBookFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class Faq_Frame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        self.faq_main_frame = tkb.Frame(root, bootstyle="dark")
        self.faq_main_frame.grid(row=0, column=1, sticky="nsew")

        self.main_label = tkb.Label(self.faq_main_frame, text="testing text")
        self.main_label.pack()






