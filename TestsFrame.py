import ttkbootstrap as tkb
from ttkbootstrap.constants import *

import tests_db
import tests_db as testdb
import QuastionsFrame as qf

def TestsFrameOn(root):
    def Tests_Main_Logic(button):
        pass
            # if button.cget("text") == "ДЕПРЕССИЯ":
            #  test = qf.QuastionFrameTest(main_test_frame, tests_db.depression_list, "Опрос: депрессия")



    # === Tests Frame ===
    # Main Test Frame
    main_test_frame = tkb.Frame(root, bootstyle='dark')
    main_test_frame.grid(row=0, column=1, sticky="nsew")

    # Main Label
    test_main_label = tkb.Label(main_test_frame, bootstyle="inverse-dark", text="ТЕСТУВАННЯ", font=("Gotham-bold", 25))
    test_main_label.pack(pady=10)
    attention_text = "Увага! Самолікування може бути шкідливим для здоров'я. " \
                     "\nРезультати тестів необхідно проаналазувати з фахівцем уникаючи гіпероцінки."

    # Info Label
    info_main_label = tkb.Label(main_test_frame, bootstyle="inverse-dark",
                                text=attention_text,
                                font=("Gotham", 10))
    info_main_label.pack(pady=10)



    # Main_Buttons Frame
    Frame_For_Buttons = tkb.Frame(main_test_frame, bootstyle='vapor')
    Frame_For_Buttons.pack(pady=20)

    # Variants List
    variants_list = ["ДЕПРЕССИЯ", "САР", "ОКР", "ПТСР",
                     "ТРЕВОЖНОЕ РАССТРОЙСТВО", "САМООЦЕНКА", "ОБЩИЙ ТЕСТ", "ПРЕРЫВАНИЕ КОНТАКТА"]

    # Button Buildings Loop
    r, c = 0, 0
    for i in range(0, 8):
        button = tkb.Button(Frame_For_Buttons, bootstyle='info', text=variants_list[i], width=30)
        button.config(command=lambda button=button: Tests_Main_Logic(button)) # Ключевой аспект в логике программы
        button.grid(row=r, column=c, padx=10, pady=10)
        r += 1
        if r == 4:
            c += 1
            r = 0
    # === Tests Frame ===
