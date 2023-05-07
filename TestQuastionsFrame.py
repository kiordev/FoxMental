# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# TestQuastionsFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *
import tests_db as tdb
import TestingWindowFrame as twf

class TestQuastionsFrame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        self.main_test_frame = tkb.Frame(root, bootstyle='dark')
        self.main_test_frame.grid(row=0, column=1, sticky="nsew")

        # Main Label
        self.test_main_label = tkb.Label(self.main_test_frame, bootstyle="inverse-dark", text="ТЕСТУВАННЯ",
                                    font=("Gotham-bold", 25))
        self.test_main_label.pack(pady=10)
        self.attention_text = "Увага! Самолікування може бути шкідливим для здоров'я. " \
                         "\nРезультати тестів необхідно проаналазувати з фахівцем уникаючи єффекту Данінга-Крюгера."

        # Info Label
        self.info_main_label = tkb.Label(self.main_test_frame, bootstyle="inverse-dark",
                                    text=self.attention_text,
                                    font=("Gotham", 10))
        self.info_main_label.pack(pady=10)

        # Main_Buttons Frame
        self.Frame_For_Buttons = tkb.Frame(self.main_test_frame, bootstyle='vapor')
        self.Frame_For_Buttons.pack(pady=20)

        # Variants List
        self.variants_list = ["ДЕПРЕСІЯ", "САР", "ОКР", "ПТСР",
                         "ТРИВОЖНИЙ РОЗЛАД", "САМООЦІНКА", "ЗАГАЛЬНИЙ ТЕСТ", "КОГНІТИВНИ СПОТВОРЕННЯ"]

        # Button Buildings Loop
        self.r, self.c = 0, 0
        for i in range(0, 8):
            button = tkb.Button(self.Frame_For_Buttons, bootstyle='info', text=self.variants_list[i], width=30)
            button.config(command=lambda button=button: self.Tests_Main_Logic(button))  # Ключевой аспект в логике программы
            button.grid(row=self.r, column=self.c, padx=10, pady=10)
            self.r += 1
            if self.r == 4:
                self.c += 1
                self.r = 0

    def Tests_Main_Logic(self, button):
        for i, test in enumerate(self.variants_list):
            if self.variants_list[i] == button["text"]:
                test = twf.TestingFrame(self.variants_list[i])
                test.mainloop()




