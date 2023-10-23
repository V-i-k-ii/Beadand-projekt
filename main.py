import tkinter as tk
from tkinter import messagebox
from file_operations import save_data_to_file, load_data_from_file

# Definiáljuk a login_username_entry és login_password_entry változókat a modul szinten
login_username_entry = None
login_password_entry = None

def save_user_data():
    name = name_entry.get()
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name and username and email and password:
        if is_username_unique(username):
            save_data_to_file(name, username, email, password)
            messagebox.showinfo("Success", "Registration successful.")
            switch_to_login_window()
        else:
            messagebox.showerror("Error", "Username already exists. Please choose a different one.")
    else:
        messagebox.showerror("Error", "All fields are required.")

def is_username_unique(username):
    data = load_data_from_file()
    usernames = [entry[1] for entry in data]
    return username not in usernames

def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Username and password are required.")
        return

    data = load_data_from_file()
    for entry in data:
        if entry[1] == username and entry[3] == password:
            messagebox.showinfo("Success", "Login successful.")
            return

    messagebox.showerror("Error", "Invalid username or password.")

def switch_to_login_window():
    global login_username_entry, login_password_entry

    # Elrejtjük a regisztrációs ablakot
    root.withdraw()

    # Létrehozzuk a bejelentkezési ablakot
    login_window = tk.Tk()
    login_window.title("User Login")

    login_username_label = tk.Label(login_window, text="Username:")
    login_username_label.pack()
    login_username_entry = tk.Entry(login_window)
    login_username_entry.pack()

    login_password_label = tk.Label(login_window, text="Password:")
    login_password_label.pack()
    login_password_entry = tk.Entry(login_window, show="*")
    login_password_entry.pack()

    def show_registration_window():
        root.deiconify()  # Visszatérünk a regisztrációs ablakhoz
        login_window.destroy()  # Bejelentkezési ablak bezárása

    login_button = tk.Button(login_window, text="Login", command=login_user)
    login_button.pack()

    # Bejelentkezési ablak bezárásakor visszatérünk a regisztrációs ablakhoz
    login_window.protocol("WM_DELETE_WINDOW", show_registration_window)

    login_window.mainloop()

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
password_entry = tk.Entry(root, show="*")
password_entry.pack()

register_button = tk.Button(root, text="Register", command=save_user_data)
register_button.pack()

login_switch_button = tk.Button(root, text="Switch to Login", command=switch_to_login_window)
login_switch_button.pack()

root.mainloop()

