# Rozs Viktória - AGH59A

A beadandó feladatomban egy egyszerű számológépet készítettem. A számológép le tudja menteni az eredményeket egy fájlba, hogy azt vissza lehessen követni, le tudja kérdezni, majd ki is tudja törölni a tartalmát.  

Modulok és hozzá tartozó függvények: 
  customtkinter:
    CTk()
    CTkButton()
    CTkEntry()
  messagebox:
    showinfo(title, message)
    showerror(title, message)
    showwarning(title, message)
  os:
    os.path.exists(filename)
    os.remove(filename)
  
  Saját modul (file_handler):
    save_result_to_file(result, filename)
    list_results_from_file(filename)

  
