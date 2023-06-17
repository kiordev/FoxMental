# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# ExpressTestingFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class ExpressTestingFrame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        # Основной фрейм
        self.faq_main_frame = tkb.Frame(root, bootstyle="dark")
        self.faq_main_frame.grid(row=0, column=1, sticky="nsew")
        # Инструкции заголовок
        self.instructions_label = tkb.Label(self.faq_main_frame, text="test", bootstyle='inverse-dark', font=("Gotham-bold", 16))
        self.instructions_label.pack(padx=10, pady=10, anchor=NW)







