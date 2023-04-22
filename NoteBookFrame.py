# -*- coding: utf-8 -*- # за каким-то хреном он тупой, и не понимает, что тут UTF-8
import ttkbootstrap as tkb
# ==========Create NoteBook_Frame=========

def NoteBookOn(root):
    notebook_main_frame = tkb.Frame(root, bootstyle="dark")
    notebook_main_frame.grid(row=0, column=1, sticky="nsew")

    # NoteBook_Frame_Name
    notebook_name_label = tkb.Label(notebook_main_frame, text="ТЕКСТ", font=("Gotham-bold", 15),
                                    bootstyle="inverse-dark")
    notebook_name_label.pack(pady=10)

    # NoteBook_Widget
    my_notebook = tkb.Notebook(notebook_main_frame, bootstyle='dark')
    my_notebook.pack(pady=20)

    # Create PAGE
    tab1 = tkb.Frame(my_notebook)
    my_notebook.add(tab1, text='NOTES')

    # Create a Text Field
    my_text = tkb.Text(tab1, height=10, width=90)
    my_text.pack()

    def save_notebook_content():
        file = open('notes.txt', 'w')
        content = my_text.get("1.0", "end-1c")
        file.write(content)

    try:
        file = open('notes.txt', 'r')
        content = file.read()
        my_text.insert('end', content)
    except FileNotFoundError:
        pass

    # Save NoteBook Text Button
    save_button = tkb.Button(notebook_main_frame, text="SAVE", bootstyle='primary', command=save_notebook_content)
    save_button.pack(pady=10)

    # ==========Create NoteBook_Widget=========

