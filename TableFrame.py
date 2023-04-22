# -*- coding: utf-8 -*- # за каким-то хреном он тупой, и не понимает, что тут UTF-8
import ttkbootstrap as tkb
import tkinter as tk
def TableFrameOn(root):
    # =======Table_Main_Frame + Table=======
    table_main_frame = tkb.Frame(root, bootstyle="dark")
    table_main_frame.grid(row=0, column=1, sticky="nsew")
    # Test_Frame_Name
    test_name_label = tkb.Label(table_main_frame, text="ТАБЛИЦЯ", font=("Gotham-bold", 15), bootstyle="inverse-dark")
    test_name_label.pack(pady=10)

    # Создание заголовков для колонок
    columns = ("Событие", "Мысли", "Эмоция", "Действие")

    # Создание таблицы
    table = tkb.Treeview(table_main_frame, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)

    # Установка ширины колонок
    table.column("Событие", width=200)
    table.column("Мысли", width=200)
    table.column("Эмоция", width=200)
    table.column("Действие", width=200)
    # Размещение таблицы
    table.pack()

    # Метод проверки контента в файле
    try:
        with open("table_data.txt", "r") as f:
            for line in f:
                row_data = line.strip().split(",")
                table.insert("", tkb.END, values=row_data)
    except FileNotFoundError:
        pass
    # =======Table_Main_Frame + Table=======

    entry_table_frame = tkb.Frame(table_main_frame, bootstyle='dark')
    entry_table_frame.pack(pady=10)

    # Entry_Widgets_For_Table
    event_entry = tkb.Entry(entry_table_frame, font=("Gotham", 12), width=10)
    event_entry.grid(row=0, column=0, padx=5)
    thoughts_entry = tkb.Entry(entry_table_frame, font=("Gotham", 12), width=10)
    thoughts_entry.grid(row=0, column=1, padx=5)
    emotion_entry = tkb.Entry(entry_table_frame, font=("Gotham", 12), width=10)
    emotion_entry.grid(row=0, column=2, padx=5)
    action_entry = tkb.Entry(entry_table_frame, font=("Gotham", 12), width=10)
    action_entry.grid(row=0, column=3, padx=5)

    def add_row():
        # Получение данных из полей ввода
        event = event_entry.get()
        thoughts = thoughts_entry.get()
        emotion = emotion_entry.get()
        action = action_entry.get()

        # Добавление новой строки в таблицу
        table.insert("", tkb.END, values=(event, thoughts, emotion, action))

        # Очистка полей ввода
        event_entry.delete(0, tkb.END)
        thoughts_entry.delete(0, tkb.END)
        emotion_entry.delete(0, tkb.END)
        action_entry.delete(0, tkb.END)

    # Table Save Data
    def save_table_data():

        with open("table_data.txt", "w") as f:
            for row_id in table.get_children():
                row_data = table.item(row_id)["values"]
                f.write(",".join(row_data) + "\n")

    # Add Record Button
    add_button = tkb.Button(table_main_frame, bootstyle='primary', text="ДОДАТИ ПОДІЮ", command=add_row)
    add_button.pack(pady=10)
    # Save Button
    save_button = tkb.Button(table_main_frame, text="ЗБЕРЕГТИ", bootstyle='primary',command=save_table_data)
    save_button.pack(pady=10)

    # Размещение таблицы на окне

