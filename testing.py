import ttkbootstrap as tkb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
# Settings
main_window = tkb.Window(themename="vapor")
main_window.geometry("1000x500")
main_window.resizable(False, False)

def Test_Main_Logic():
    if variants_buttons_list.test_name == "РАССТРОЙСТВО А":
        print("РАССТРОЙСТВО А")

class Test:

    # Создание кнопки
    def __init__(self, spawn_frame, test_name, r, c):
        tkb.Button(spawn_frame, bootstyle='danger', width=20, text=test_name, command=Test_Main_Logic).grid(row=r, column=c, padx=10, pady=10)
        self.test_name = test_name

# Список расстройств
variants_list = ["РАССТРОЙСТВО А", "РАССТРОЙСТВО B", "РАССТРОЙСТВО C", "РАССТРОЙСТВО D", "РАССТРОЙСТВО E", "РАССТРОЙСТВО F", "РАССТРОЙСТВО G", "РАССТРОЙСТВО H"]

# Расстройства по кнопкам
variants_buttons_list = []

r, c = 0, 0
for i in range(0, 8):
    variants_buttons_list.append(Test(main_window, variants_list[i], r, c))
    r += 1
    if r == 4:
        c += 1
        r = 0

print(variants_buttons_list)
# Execute
main_window.mainloop()
