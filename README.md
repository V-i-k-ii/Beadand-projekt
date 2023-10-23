# Rozs Viktória - AGH59A

A beadandó feladatomban egy egyszerű regisztrációs felületet készítettem, ahol a felhasználó az adatai megadásával(név, felhasználónév, e-mail, jelszó) tud regisztrálni, majd belépni. 

Modulok és hozzá tartozó függvények: 
  tkinter:
    TK()
    Label()
    Entry()
    Button()
    pack()
  messagebox:
    showinfo(title, message)
    showerror(title, message)
  file_operations:
    save_data_to_file(name, username, email, password)
    load_data_from_file()
    is_username_unique(username)
