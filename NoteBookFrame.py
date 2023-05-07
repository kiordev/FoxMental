# Дипломний проект [PYTHON, TKINTER, TTKBOOTSTRAP] | NAME: "MENTALA"
# NoteBookFrame
# Кіор Олександр Сергійович, ВТ-19, 20.04.2023

import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class NoteBookFrame(tkb.Frame):
    def __init__(self, root):
        super().__init__()
        self.notebook_main_frame = tkb.Frame(root, bootstyle="dark")
        self.notebook_main_frame.grid(row=0, column=1, sticky="nsew")

        # NoteBook_Frame_Name
        self.notebook_name_label = tkb.Label(self.notebook_main_frame, text="ТЕКСТ", font=("Gotham-bold", 15),
                                        bootstyle="inverse-dark")
        self.notebook_name_label.pack(pady=10)

        # NoteBook_Widget
        self.my_notebook = tkb.Notebook(self.notebook_main_frame, bootstyle='dark')
        self.my_notebook.pack(pady=20)

        # Create PAGE
        self.tab1 = tkb.Frame(self.my_notebook)
        self.my_notebook.add(self.tab1, text='NOTES')

        # Create a Text Field
        self.my_text = tkb.Text(self.tab1, height=10, width=90)
        self.my_text.pack()

        # Save NoteBook Text Button
        self.save_button = tkb.Button(self.notebook_main_frame, text="ЗБЕРЕГТИ", bootstyle='primary',
                                      command=self.save_notebook_content)
        self.save_button.pack(pady=10)

        # CheckNoteBookContent
        try:
            file = open('notes.txt', 'r')
            content = file.read()
            self.my_text.insert('end', content)
        except FileNotFoundError:
            pass

    def save_notebook_content(self):
        file = open('notes.txt', 'w')
        content = self.my_text.get("1.0", "end-1c")
        file.write(content)





