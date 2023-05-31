import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


#Limits
MAX_NUMBER = 500
MIN_NUMBER = 1

#List to store submissions
submissions = []

#Validation Check (Only Letters)
def validate_name_entry(text):
    if any(char.isdigit() or (not char.isalnum() and char != " ") for char in text):
        messagebox.showerror("Error", "Numbers and symbols are not allowed in the Customer's Full Name.")
        return False
    return True

def validate_item_entry(text):
    if any(char.isdigit() or (not char.isalpha() and char != " ") for char in text):
        messagebox.showerror("Error", "Numbers and symbols are not allowed in the Item Hired.")
        return False
    
def submit_info():
    name = name_entry.get()
    amount = no_items_entry.get()
    receipt = receipt_no_entry.get()
    item = item_entry.get()
    try:
        #IF statements for error messages
        #Empty Entries
        if not name:
            raise ValueError("Please fill in the Customer's Full Name.")

        if not receipt:
            raise ValueError("Please fill in the Receipt Number.")

        if not amount:
            raise ValueError("Please fill in the Items Hired.")

        if not item:
            raise ValueError("Please fill in the Quantity of Items hired.")
        #Validation Check (Numbers Only)
        if not receipt.isdigit():
            raise ValueError("Invalid receipt number. Digits only.")

        if not amount.isdigit() or int(amount) < MIN_NUMBER or int(amount) > MAX_NUMBER:
            raise ValueError(f"Invalid Quantity. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.")

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

    except ValueError as e:
        
#Display error message
        error_label.config(text=str(e))

#Delete Function
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select the item to be deleted.")
        return
    index = int(tree.index(selected_item))
    del submissions[index]  # Remove submission from the list
    tree.delete(selected_item)

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

#Item Label
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

#Validation Checks Link with Entries
name_entry['validatecommand'] = (name_entry.register(validate_name_entry), '%P')
name_entry['validate'] = 'key'
item_entry['validatecommand'] = (name_entry.register(validate_item_entry), '%P')
item_entry['validate'] = 'key'

#Buttons
#Button 1 (Delete)
delete_button = tk.Button(root, text='Delete',command=delete_info)
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
