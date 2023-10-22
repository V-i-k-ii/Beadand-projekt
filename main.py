import tkinter as tk
from tkinter import messagebox
from file_operations import save_data_to_file, load_data_from_file

def save_user_data():
    name = name_entry.get()
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name and username and email and password:
        if is_username_unique(username):
            save_data_to_file(name, username, email, password)
            messagebox.showinfo("Success", "Registration successful.")
        else:
            messagebox.showerror("Error", "Username already exists. Please choose a different one.")
    else:
        messagebox.showerror("Error", "Name, username, email, and password are required.")

def is_username_unique(username):
    data = load_data_from_file()
    usernames = [entry[1] for entry in data]
    return username not in usernames

def load_user_data():
    data = load_data_from_file()
    if data:
        data_str = "User Data:\n"
        for name, username, email, password in data:
            data_str += f"Name: {name}, Username: {username}, E-mail: {email}, Password: {password}\n"
        messagebox.showinfo("User Data", data_str)
    else:
        messagebox.showinfo("User Data", "No data found!")

root = tk.Tk()
root.title("User Registration")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Jelszó elrejtése
password_entry.pack()

register_button = tk.Button(root, text="Register", command=save_user_data)
register_button.pack()

load_button = tk.Button(root, text="Load Data", command=load_user_data)
load_button.pack()

root.mainloop()