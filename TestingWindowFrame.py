# Окно для прохождения тестирования
# TestingWindowFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

# Imports
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

import tests_db

class TestingFrame(tkb.Toplevel):
    def __init__(self, test_list, test_title):
        super().__init__()
        # Window Settings
        self.geometry('400x850+1400+200')
        self.title("Тестування")
        self.resizable(False, False)
        self.style.theme_use('vapor')
        self.score = 0
        self.test_list = test_list
        self.test_title = test_title
        print(test_list)

        # Test Name Label
        self.main_label = tkb.Label(self, text=test_title, font=("Gotham-bold", 15), bootstyle='danger')
        self.main_label.pack(pady=10)

        # Qustions_Frame
        self.quastions_frame = tkb.Frame(self, bootstyle="dark")
        self.quastions_frame.pack(pady=10)

        # Check_Buttons_Score_Control
        self.score_list = [0]

        # Add Quastions Loop
        self.vars = []
        for i, quastion in enumerate(self.test_list):
            var = tkb.IntVar()
            self.vars.append(var)
            tkb.Checkbutton(self.quastions_frame,
                            bootstyle='primary', variable=var,
                            text=quastion,
                            offvalue=0,
                            onvalue=1).grid(row=i, column=1, padx=10, pady=10)

        # Result Frame
        self.result_frame = tkb.Frame(self, bootstyle="vapor")
        self.result_frame.pack()

        # Result Button
        self.result_button = tkb.Button(self.result_frame, text="РЕЗУЛЬТАТ", bootstyle='primary', command=self.check_result)
        self.result_button.pack(pady=10)

        # Meter Widget For Score
        self.result_score_meter = tkb.Meter(self.result_frame,
                                            subtext='Результат',
                                            interactive=False,
                                            bootstyle='success',
                                            stripethickness=10,
                                            textright='sec',
                                            amounttotal=12,
                                            metersize=180)

        self.result_score_meter.pack(pady=10)

    # def check_result
    def check_result(self):
        total = sum([var.get() for var in self.vars])
        self.result_score_meter.configure(amountused=total)
        if self.result_score_meter["amountused"] >=5:
            self.result_score_meter.configure(bootstyle='danger')
        else:
            self.result_score_meter.configure(bootstyle='success')



if __name__ == "__main__":
    app = TestingFrame(tests_db.depression_list, "ДЕПРЕССИЯ")
    app.mainloop()
