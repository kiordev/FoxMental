# -*- coding: utf-8 -*- # за каким-то хреном он тупой, и не понимает, что тут UTF-8
import ttkbootstrap as tkb
from ttkbootstrap.constants import *

def TestsFrameOn(root):
    # ==========Tests_Frame=========
    tests_main_frame = tkb.Frame(root, bootstyle="dark")
    tests_main_frame.grid(row=0, column=1, sticky="nsew")
    # Test_Frame_Name
    test_name_label = tkb.Label(tests_main_frame, text="ТЕСТУВАННЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
    test_name_label.pack(pady=10)

    test_buttons_frame = tkb.Frame(tests_main_frame, bootstyle='light')
    test_buttons_frame.pack(expand=True, fill=BOTH)

    test_name_lists = ["ОКР", "САР", "ДЕПРЕССИЯ", "ТРЕВОЖНОСТЬ", "ПТСР",
                       "АЛЬФА РАССТРОЙСТВО",
                       "БЕТА РАССТРОЙСТВО",
                       "ЗЕТА РАССТРОЙСТВО"]
    r,c = 0, 0
    for i in range(0, 2):
        tkb.Button(test_buttons_frame, bootstyle="danger-outline", text=test_name_lists[i] width=10).gr
    # ==========Tests_Frame=========