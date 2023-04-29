# Окно для прохождения тестирования
# TestingWindowFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

# Imports
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

import tests_db
import tests_db as tdb

class TestingFrame(tkb.Toplevel):
    def __init__(self, test_title):
        super().__init__()
        # Window Settings
        self.geometry('900x850+1400+200')
        self.title("Тестування")
        self.resizable(False, False)
        self.score = 0
        self.test_title = test_title

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
        for test, quastions in tdb.TEST_DATABASE.items():
            if test == self.test_title:
                i = 0
                for quastion in quastions:
                    var = tkb.IntVar()
                    self.vars.append(var)
                    tkb.Checkbutton(self.quastions_frame,
                                         bootstyle='primary', variable=var,
                                         text=quastion,
                                         offvalue=0,
                                         onvalue=1).grid(row=i, column=1, padx=10, pady=10, sticky="w")
                    i += 1
                    print(i)
            else:
                print(self.test_title)



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
                                            textright='',
                                            amounttotal=12,
                                            metersize=250)

        self.result_score_meter.pack(pady=10)

    # def check_result
        self.result_label = tkb.Label(self.result_frame, text='', bootstyle='success', font=("Gotham-bold", 20))
        self.result_label.pack(pady=5)
    def check_result(self):
        total = sum([var.get() for var in self.vars])
        self.result_score_meter.configure(amountused=total)
        if self.result_score_meter["amountused"] >=8:
            self.result_score_meter.configure(bootstyle='danger')
            self.result_label.config(text="Потрібна термінова допомога фахівця!", bootstyle='danger')
        elif self.result_score_meter["amountused"] >=5:
            self.result_score_meter.configure(bootstyle='warning')
            self.result_label.config(text="Краще звернутися до спеціаліста", bootstyle='warning')
        else:
            self.result_score_meter.configure(bootstyle='success')
            self.result_label.config(text="Варіант норми, або інша симптоматика", bootstyle='success')



if __name__ == "__main__":
    app = TestingFrame("ДЕПРЕССИЯ")
    app.mainloop()
