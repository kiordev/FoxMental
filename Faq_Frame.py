# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# NoteBookFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class Faq_Frame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        # Основной фрейм
        self.faq_main_frame = tkb.Frame(root, bootstyle="dark")
        self.faq_main_frame.grid(row=0, column=1, sticky="nsew")
        # Инструкции заголовок
        self.instructions_label = tkb.Label(self.faq_main_frame,
                                            text="ІНСТРУКЦІЇ ТА ПРАВИЛА ВИКОРИСТАННЯ",
                                            bootstyle='inverse-dark',
                                            font=("Gotham-bold", 16))
        self.instructions_label.pack(padx=10,pady=10, anchor=NW)
        # Попередження
        self.warning_label = tkb.Label(self.faq_main_frame,
                                            text="Попередження",
                                            bootstyle='inverse-dark',
                                            font=("Gotham-bold", 12))
        self.warning_label.pack(padx=10, pady=10, anchor=NW)
        # Текст попередження
        self.warning_texts = "1) Додаток знаходиться у прототипній версії для тестування; \n"\
                             "2) Під час тестування, використання цього додатка не є безпечним для вашого здоров'я; \n"\
                             "3) Не зволікайте піти на консультацію до спеціалиста; \n"\
                             "4) Результат проходження тестування - не є клінічним діагнозом; \n"\
                             "5) У вкладках Нотатник та Таблиця на забувайте тиснути на кнопку ЗБЕРЕГТИ  (приклад нижче); \n"\
                             "6) Для видалення інформації з таблиці, треба стерти контент у файлі table_data.txt; \n"
        self.warning_text = tkb.Label(self.faq_main_frame, text=self.warning_texts, bootstyle='inverse-dark', font=("Gotham", 12))
        self.warning_text.pack(padx=10, pady=3, anchor=NW)
        # Кнопка зберегти для прикладу
        self.save_button = tkb.Button(self.faq_main_frame, text="ЗБЕРЕГТИ", bootstyle='primary')
        self.save_button.pack(padx=10, pady=3)


        # Separator
        self.menu_separator = tkb.Separator(self.faq_main_frame, bootstyle='primary')
        self.menu_separator.pack(fill='x', pady=10)

        # Новини заголовок
        self.news_label = tkb.Label(self.faq_main_frame,
                                            text="НОВИНИ 17.06.2023",
                                            bootstyle='inverse-dark',
                                            font=("Gotham-bold", 16))
        self.news_label.pack(padx=10, pady=10, anchor=NW)

        # Текст новин
        self.news_texts = "Додаток оновлено до версії 1.2.5: \n" \
                             " - Додана нова вкладка з інструкціями; \n" \
                             " - Додан Scrollbar для таблиці; \n" \
                             " - Додана можливість вписувати дату у таблицю; \n" \
                             "Слідкуйте за ходом розробки та новинами у Telegram: https://t.me/psyhoproger"
        self.news_text = tkb.Label(self.faq_main_frame, text=self.news_texts, bootstyle='inverse-dark',
                                      font=("Gotham", 12))
        self.news_text.pack(padx=10, pady=3, anchor=NW)






