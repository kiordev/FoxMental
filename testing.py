import tkinter as tk
from tkinter import ttk

def create_treeview(root):
    # Create the Treeview widget
    treeview = ttk.Treeview(root)
    treeview.pack(fill='both', expand=True)

    # Configure the columns
    treeview['columns'] = ('column1', 'column2', 'column3')
    treeview.column('#0', width=100)
    treeview.column('column1', width=100)
    treeview.column('column2', width=100)
    treeview.column('column3', width=100)
    treeview.heading('#0', text='ID')
    treeview.heading('column1', text='Column 1')
    treeview.heading('column2', text='Column 2')
    treeview.heading('column3', text='Column 3')

    # Apply color to specific columns
    treeview.heading('column1', text='Column 1', command=lambda: apply_column_color(treeview, 'column1', 'red'))
    treeview.heading('column2', text='Column 2', command=lambda: apply_column_color(treeview, 'column2', 'green'))
    treeview.heading('column3', text='Column 3', command=lambda: apply_column_color(treeview, 'column3', 'blue'))

    # Insert sample data
    for i in range(1, 21):
        item = treeview.insert('', 'end', text=f'Item {i}')
        treeview.set(item, 'column1', f'Value 1-{i}')
        treeview.set(item, 'column2', f'Value 2-{i}')
        treeview.set(item, 'column3', f'Value 3-{i}')

def apply_column_color(treeview, column_id, color):
    # Configure tag styles for the column
    treeview.tag_configure(column_id, background=color)

    # Apply the tag to all cells in the column
    for item_id in treeview.get_children():
        treeview.item(item_id, tags=(column_id,))

# Create the main window
root = tk.Tk()

# Create the Treeview widget
create_treeview(root)

# Start the Tkinter event loop
root.mainloop()
