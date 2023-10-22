import tkinter as tk
from tkinter import messagebox
from file_operations import save_data_to_file, load_data_from_file

def save_user_data():
    name = name_entry.get()
    age = age_entry.get()

    if name and age:
        save_data_to_file(name, age)
        messagebox.showinfo("Success", "Data saved successfully.")
    else:
        messagebox.showerror("Error", "Both name and age are required.")

def load_user_data():
    data = load_data_from_file()
    messagebox.showinfo("User Data", data)

root = tk.Tk()
root.title("User Data Management")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

save_button = tk.Button(root, text="Save Data", command=save_user_data)
save_button.pack()

load_button = tk.Button(root, text="Load Data", command=load_user_data)
load_button.pack()

root.mainloop()