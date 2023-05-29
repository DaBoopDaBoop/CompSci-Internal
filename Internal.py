import tkinter as tk
from tkinter import ttk

#Windows
root = tk.Tk()
root.geometry("800x500")
root.title("Julies Party Store")
root.resizable(False, False)

#Labels
#Location Label
name_label = tk.Label(root, text="Customer name:")
name_label.grid(row=2, column=2)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=3)

#No.Group Members Label
no_items_label = tk.Label(root, text="Amount of Items:")
no_items_label.grid(row=3, column=2)
no_items_entry = tk.Entry(root)
no_items_entry.grid(row=3, column=3)

#Name of Group Label
receipt_no_label = tk.Label(root, text="Receipt Number:")
receipt_no_label.grid(row=4, column=2)
receipt_no_entry = tk.Entry(root)
receipt_no_entry.grid(row=4, column=3)

#Weather Label
item_label = tk.Label(root, text="Item Hired:")
item_label.grid(row=5, column=2)
item_entry = tk.Entry(root)
item_entry.grid(row=5, column=3)

#Title Label
label = tk.Label(root, text="Julies Party Hire", font=("times, 20"))
label.grid(row=1, column=2, columnspan=4, padx=10, pady=10)

# Error Label
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=8, column=2, columnspan=2)