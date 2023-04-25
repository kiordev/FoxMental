# import ttkbootstrap as tkb
# from ttkbootstrap.constants import *
# import TestsFrame as tf
# import tests_db
#
# class QuastionFrameTest(tkb.Window):
#     quastion_list = []
#     quastion_score = None
#     main_testing_quastion_frame = None
#     finish_button = None
#     master = None
#     opros_label = None
#
#     def __init__(self, master, quastion_from_db, test_name):
#         super().__init__()
#         self.title(test_name)
#         self.style.theme_use("vapor")
#         self.geometry("800x1000")
#
#         # Custom Parameters
#         self.test_name = test_name
#         self.master = master
#         self.quastion_list = quastion_from_db # Присвоение списка вопросов в класс
#
#         # Создание фрейма
#         self.main_testing_quastion_frame = tkb.Frame(self.master, bootstyle="vapor")
#         self.main_testing_quastion_frame.pack(pady=10)
#
#         # Название теста
#         self.opros_label = tkb.Label(self.master, text=self.test_name, bootstyle='danger', font=('Gotham', 10))
#         self.opros_label.pack(pady=10)
#
#         # Создание списка вопросов
#         for i, quastion in enumerate(self.quastion_list):
#             tkb.Label(self.main_testing_quastion_frame,
#                       text=quastion,
#                       bootstyle='danger', font=('Gotham', 10)).grid(row=i, column=0)
#             tkb.Checkbutton(self.main_testing_quastion_frame, bootstyle='danger', text="Да").grid(row=i, column=1)
#
#         # Кнопка закончить
#         self.finish_button = tkb.Button(master, text="Закончить")
#         self.finish_button.pack()
#
# # Инициализация программы
# root = tkb.Window()
# app = QuastionFrameTest(root, tests_db.depression_list, "Опрос: депрессия")
# app.mainloop()




