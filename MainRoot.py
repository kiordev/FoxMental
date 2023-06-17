# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *
import NoteBookFrame as nbf
import TableFrame as tb
import TestQuastionsFrame as tqf
import Faq_Frame as ff

class MainRoot(tkb.Window):
    def __init__(self):
        super().__init__()
        # Main_Root_Settings
        self.style.theme_use('vapor')
        self.geometry("1400x600+300+200")
        self.resizable(False, False)
        self.title("FoxMental")

        # Root_Grid_Configure
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=10)

        # ------Menu_Frame------
        self.menu_frame = tkb.Frame(self)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # Menu Label
        self.menu_label = tkb.Label(self.menu_frame, text="ГОЛОВНЕ МЕНЮ", font=("Gotham-bold", 10), bootstyle="primary")
        self.menu_label.pack(pady=10)

        # Start_Test_Button
        self.test_button = tkb.Button(self.menu_frame, text='ПРОЙТИ ТЕСТ', bootstyle="primary", width=20, command=self.test_on)
        self.test_button.pack(pady=10)

        # Start_Table_Button
        self.table_button = tkb.Button(self.menu_frame, text='ТАБЛИЦЯ', bootstyle="primary", width=20, command=self.table_on)
        self.table_button.pack(pady=10)

        # Start_NoteBook_Button
        self.notebook_button = tkb.Button(self.menu_frame, text='НОТАТКИ', bootstyle="primary", width=20, command=self.notebook_on)
        self.notebook_button.pack(pady=10)

        # Start_Faq_Button
        self.faq_button = tkb.Button(self.menu_frame, text='FAQ', bootstyle="primary", width=20,command=self.faq_on)
        self.faq_button.pack(pady=10)

        # Separator
        self.menu_separator = tkb.Separator(self.menu_frame, bootstyle='primary')
        self.menu_separator.pack(fill='x', pady=10)

        # Settings Label
        self.settings_label = tkb.Label(self.menu_frame, text="НАЛААШТУВАННЯ", font=("Gotham-bold", 10), bootstyle="primary")
        self.settings_label.pack(pady=10)

        # Theme Combo Box
        self.my_theme = self.style.theme_names()
        self.theme_combobox = tkb.Combobox(self.menu_frame, values=self.my_theme)
        self.theme_combobox.pack(pady=5, padx=10)
        self.accept_theme_button = tkb.Button(self.menu_frame, bootstyle='primary', text='ПРИЙНЯТИ ТЕМУ', command=self.accept_theme)
        self.accept_theme_button.pack(pady=10, padx=10)
        self.theme_combobox.current(15)

        # Version_Label
        self.version_label = tkb.Label(self.menu_frame, text="FoxMental | 1.2.5 | WINDOWS ver", font=("Gotham", 10), bootstyle="primary")
        self.version_label.pack(anchor="s", side=tkb.BOTTOM, padx=10)

        # Methods
    def test_on(self):
        test = tqf.TestQuastionsFrame(self)
        test.tkraise()

        # On_NoteBook_Frame
    def notebook_on(self):
        notebook = nbf.NoteBookFrame(self)
        notebook.tkraise()

        # On_Table_Frame
    def table_on(self):
        table = tb.TableFrame(self)
        table.tkraise()

    def faq_on(self):
        faq = ff.Faq_Frame(self)
        faq.tkraise()

        # Accept Theme
    def accept_theme(self):
        self.style.theme_use(themename=self.my_theme[self.theme_combobox.current()])

if __name__ == "__main__":
    app = MainRoot()
    app.mainloop()