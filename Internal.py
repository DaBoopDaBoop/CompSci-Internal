import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


#Limits
MAX_NUMBER = 500
MIN_NUMBER = 1

#List to store submissions
submissions = []

def submit_info():
    name = name_entry.get()
    amount = no_items_entry.get()
    receipt = receipt_no_entry.get()
    item = item_entry.get()
   
# Get current time
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Add submission to the list
    submissions.append((name, amount, receipt, item, time))

#Clear entry fields
    name_entry.delete(0, tk.END)
    no_items_entry.delete(0, tk.END)
    receipt_no_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)

#Update Treeview
    tree.insert("", tk.END, values=(name, amount, receipt, item, time))


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

#Buttons
#Button 1 (Delete)
delete_button = tk.Button(root, text='Delete')
delete_button.grid(row=6, column=2, padx=5, pady=5)

#Button 2 (Add)
add_button = tk.Button(root, text='Add',command=submit_info)
add_button.grid(row=6, column=3, padx=5, pady=5)

tree = ttk.Treeview(root, show="headings")
tree["columns"] = ("Customer Name", "Amount of Items", "Receipt Number", "Item Hired", "Time")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Customer Name", width=100)
tree.column("Amount of Items", width=200)
tree.column("Receipt Number", width=150)
tree.column("Item Hired", width=200)
tree.column("Time", width=200)
tree.heading("Customer Name", text="Customer Name", anchor=tk.CENTER)
tree.heading("Amount of Items", text="Amount of Items", anchor=tk.CENTER)
tree.heading("Receipt Number", text="Receipt Number", anchor=tk.CENTER)
tree.heading("Item Hired", text="Item Hired", anchor=tk.CENTER)
tree.heading("Time", text="Time", anchor=tk.CENTER)
tree.grid(row=7, column=2, columnspan=3, padx=10, pady=10)

root.mainloop()
