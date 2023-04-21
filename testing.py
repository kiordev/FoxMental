import tkinter as tk
import ttkbootstrap as ttkbs


class NoteBookApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notebook App")

        # Создаем Notebook виджет
        self.notebook = ttkbs.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Создаем вкладку для записей
        self.notes_tab = ttkbs.Frame(self.notebook)
        self.notebook.add(self.notes_tab, text='Notes')

        # Создаем текстовое поле для записей
        self.notes_text = tk.Text(self.notes_tab, height=10, width=50)
        self.notes_text.pack(side="left", fill="both", expand=True)

        # Создаем кнопку для сохранения записей
        save_button = ttkbs.Button(self.notes_tab, text="Save", command=self.save_notes)
        save_button.pack(side="right")

        # Загружаем предыдущие записи, если они есть
        try:
            with open("saved_notes.txt", "r") as f:
                notes = f.read()
                self.notes_text.insert("end", notes)
        except FileNotFoundError:
            pass

    def save_notes(self):
        # Получаем содержимое текстового поля
        notes = self.notes_text.get("1.0", "end-1c")
        # Сохраняем записи в файл
        with open("saved_notes.txt", "w") as f:
            f.write(notes)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = NoteBookApp()
    app.run()