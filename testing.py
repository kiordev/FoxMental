import ttkbootstrap as tkb

# Создание окна
root = tkb.Window()
root.title("Моя таблица")

# Создание фрейма для таблицы
table_frame = tkb.Frame(root, bootstyle='dark')
table_frame.pack(pady=20)

# Создание заголовков для колонок
columns = ("Событие", "Мысли", "Эмоция", "Действие")

# Создание таблицы
table = tkb.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)

# Установка ширины колонок
table.column("Событие", width=200)
table.column("Мысли", width=200)
table.column("Эмоция", width=200)
table.column("Действие", width=200)

# Загрузка данных из файла, если он существует
try:
    with open("table_data.txt", "r") as f:
        for line in f:
            row_data = line.strip().split(",")
            table.insert("", tkb.END, values=row_data)
except FileNotFoundError:
    pass

# MAIN_TABLE_ENTRIES
event_entry = tkb.Entry(root, font=("Arial", 12), width=30)
event_entry.pack(pady=10)
thoughts_entry = tkb.Entry(root, font=("Arial", 12), width=30)
thoughts_entry.pack(pady=10)
emotion_entry = tkb.Entry(root, font=("Arial", 12), width=30)
emotion_entry.pack(pady=10)
action_entry = tkb.Entry(root, font=("Arial", 12), width=30)
action_entry.pack(pady=10)
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

def save_table_data():
    # Сохранение данных таблицы в файл
    with open("table_data.txt", "w") as f:
        for row_id in table.get_children():
            row_data = table.item(row_id)["values"]
            f.write(",".join(row_data) + "\n")

# Размещение кнопок на окне
add_button = tkb.Button(root, text="Добавить", command=add_row)
add_button.pack(pady=10)

save_button = tkb.Button(root, text="Сохранить", command=save_table_data)
save_button.pack(pady=10)

# Размещение таблицы на окне
table.pack()

# Запуск главного цикла
root.mainloop()