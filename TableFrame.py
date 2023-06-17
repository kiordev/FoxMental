# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# NoteBookFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class TableFrame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        # =======Table_Main_Frame + Table=======
        self.table_main_frame = tkb.Frame(root, bootstyle="dark")
        self.table_main_frame.grid(row=0, column=1, sticky="nsew")

        # Test_Frame_Name
        self.test_name_label = tkb.Label(self.table_main_frame, text="ТАБЛИЦЯ", font=("Gotham-bold", 15),
                                    bootstyle="inverse-dark")
        self.test_name_label.pack(pady=10)

        # Создание заголовков для колонок
        columns = ("Дата", "Ситуація", "Думки", "Эмоція", "Реакція")

        # Скролл бар для таблицы
        scrollbar = tkb.Scrollbar(self.table_main_frame)
        scrollbar.pack(side='right', fill='y')

        # Создание таблицы
        self.table = tkb.Treeview(self.table_main_frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
        for col in columns:
            self.table.heading(col, text=col)

        # Configure the scrollbar to scroll the treeview
        scrollbar.config(command=self.table.yview)

        # Установка ширины колонок
        self.table.column("Дата", width=200)
        self.table.column("Ситуація", width=200)
        self.table.column("Думки", width=200)
        self.table.column("Эмоція", width=200)
        self.table.column("Реакція", width=200)
        # Размещение таблицы
        self.table.pack()

        # Метод проверки контента в файле
        try:
            with open("table_data.txt", "r", encoding='cp1251') as f:
                for line in f:
                    row_data = line.strip().split(",")
                    self.table.insert("", tkb.END, values=row_data)
        except FileNotFoundError:
            pass
        # =======Table_Main_Frame + Table=======

        self.entry_table_frame = tkb.Frame(self.table_main_frame, bootstyle='dark')
        self.entry_table_frame.pack(pady=10)

        # Entry Widget names
        self.name_label_list = ["Дата", "Ситуація", "Думки", "Эмоція", "Реакція"]
        for i in range(len(self.name_label_list)):
            name = self.name_label_list[i]
            tkb.Label(self.entry_table_frame,
                      text=name, bootstyle="inverse-dark",
                      font=("Gotham-bold", 10)).grid(row=0, column=i, padx=5)

        # Entry_Widgets_For_Table
        self.date_entry = tkb.Entry(self.entry_table_frame, font=("Gotham", 12), width=10)
        self.date_entry.grid(row=1, column=0, padx=5, pady=5)
        self.event_entry = tkb.Entry(self.entry_table_frame, font=("Gotham", 12), width=10)
        self.event_entry.grid(row=1, column=1, padx=5, pady=5)
        self.thoughts_entry = tkb.Entry(self.entry_table_frame, font=("Gotham", 12), width=10)
        self.thoughts_entry.grid(row=1, column=2, padx=5, pady=5)
        self.emotion_entry = tkb.Entry(self.entry_table_frame, font=("Gotham", 12), width=10)
        self.emotion_entry.grid(row=1, column=3, padx=5, pady=5)
        self.action_entry = tkb.Entry(self.entry_table_frame, font=("Gotham", 12), width=10)
        self.action_entry.grid(row=1, column=4, padx=5, pady=5)

        # Add Record Button
        self.add_button = tkb.Button(self.table_main_frame, bootstyle='primary', text="ДОДАТИ ПОДІЮ", command=self.add_row)
        self.add_button.pack(pady=10)
        # Save Button
        self.save_button = tkb.Button(self.table_main_frame, text="ЗБЕРЕГТИ", bootstyle='primary',
                                 command=self.save_table_data)
        self.save_button.pack(pady=10)
        # Saved Message
        self.saved_message_label = tkb.Label(self.table_main_frame, text="ЗБЕРЕЖЕНО!", bootstyle="inverse-dark", font=("Gotham-bold", 10))


    def add_row(self):
         # Получение данных из полей ввода
        self.date = self.date_entry.get()
        self.event = self.event_entry.get()
        self.thoughts = self.thoughts_entry.get()
        self.emotion = self.emotion_entry.get()
        self.action = self.action_entry.get()

        # Добавление новой строки в таблицу
        self.table.insert("", tkb.END, values=(self.date, self.event, self.thoughts, self.emotion, self.action))

        # Очистка полей ввода
        self.date_entry.delete(0, tkb.END)
        self.event_entry.delete(0, tkb.END)
        self.thoughts_entry.delete(0, tkb.END)
        self.emotion_entry.delete(0, tkb.END)
        self.action_entry.delete(0, tkb.END)

        # Table Save Data
    def save_table_data(self):
        self.saved_message_label.pack(pady=10)
        with open("table_data.txt", "w") as f:
            for row_id in self.table.get_children():
                row_data = self.table.item(row_id)["values"]
                f.write(",".join(row_data) + "\n")








