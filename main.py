import customtkinter #pip install customtkinter, packaging
from tkinter import *
from tkinter import messagebox

def button_click(number):
    equation_entry.insert(END,number)

def clear():
    equation_entry.delete(0, END)

def calculate():
    try:
        equation = equation_entry.get()
        new_equation = equation.replace("X","*")
        result = eval(new_equation)
        clear()
        equation_entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "0-val nem osztunk!")
    except:
        messagebox.showerror("Error", "Adjon meg valid értékeket!")

def save_result():
    result = equation_entry.get()
    with open("szamologep_eredmeny.txt", "a") as file:
        file.write(result + '\n')  # Új sorban fűzi hozzá az eredményt
    messagebox.showinfo("Mentés", "Eredmény mentve!")

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # CTk window készítés, úgy mint Tk
app.title("Calculator")
app.geometry("300x300")
app.config(bg="#FF9912")

font1 = ("Arial", 20, "bold")

equation_entry = customtkinter.CTkEntry(app, font=font1, text_color="#000", fg_color="#fff", border_color="#000", bg_color="#FF9912", width=280, height=50)
equation_entry.place(x=10, y=10)

b1_button = customtkinter.CTkButton(app, command=lambda: button_click("7"), font=font1, text_color="#fff", text="7", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b1_button.place(x=10, y=80)

b2_button = customtkinter.CTkButton(app, command=lambda: button_click("8"), font=font1, text_color="#fff", text="8", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", corner_radius=10, border_width=2, cursor= "hand2", width=60)
b2_button.place(x=80, y=80)

b3_button = customtkinter.CTkButton(app, command=lambda: button_click("9"), font=font1, text_color="#fff", text="9", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b3_button.place(x=150, y=80)

b4_button = customtkinter.CTkButton(app, command=lambda: button_click("4"), font=font1, text_color="#fff", text="4", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b4_button.place(x=10, y=125)

b5_button = customtkinter.CTkButton(app, command=lambda: button_click("5"), font=font1, text_color="#fff", text="5", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b5_button.place(x=80, y=125)

b6_button = customtkinter.CTkButton(app, command=lambda: button_click("6"), font=font1, text_color="#fff", text="6", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b6_button.place(x=150, y=125)

b7_button = customtkinter.CTkButton(app, command=lambda: button_click("1"), font=font1, text_color="#fff", text="1", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b7_button.place(x=10, y=170)

b8_button = customtkinter.CTkButton(app, command=lambda: button_click("2"), font=font1, text_color="#fff", text="2", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b8_button.place(x=80, y=170)

b9_button = customtkinter.CTkButton(app, command=lambda: button_click("3"), font=font1, text_color="#fff", text="3", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b9_button.place(x=150, y=170)

b10_button = customtkinter.CTkButton(app, command=lambda: button_click("0"), font=font1, text_color="#fff", text="0", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", border_color="#000", border_width=2, cursor= "hand2", width=60)
b10_button.place(x=10, y=215)

b11_button = customtkinter.CTkButton(app, command=lambda: button_click("."), font=font1, text_color="#fff", text=".", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b11_button.place(x=80, y=215)

b12_button = customtkinter.CTkButton(app, command=clear, font=font1, text_color="#fff", text="C", fg_color="red", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b12_button.place(x=150, y=215)

b13_button = customtkinter.CTkButton(app, font=font1, command=calculate, text_color="#fff", text="=", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=170)
b13_button.place(x=110, y=255)

b14_button = customtkinter.CTkButton(app, command=lambda: button_click("+"), font=font1, text_color="#fff", text="+", fg_color="green", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b14_button.place(x=220, y=80)

b15_button = customtkinter.CTkButton(app, command=lambda: button_click("-"), font=font1, text_color="#fff", text="-", fg_color="green", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b15_button.place(x=220, y=125)

b16_button = customtkinter.CTkButton(app, command=lambda: button_click("X"), font=font1, text_color="#fff", text="x", fg_color="green", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b16_button.place(x=220, y=170)

b17_button = customtkinter.CTkButton(app, command=lambda: button_click("/"), font=font1, text_color="#fff", text="/", fg_color="green", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=60)
b17_button.place(x=220, y=215)

save_button = customtkinter.CTkButton(app, command=save_result, text="Mentés", font=font1, text_color="#fff", fg_color="#323d3b", hover_color="#05b314", bg_color="#FF9912", corner_radius=10, border_color="#000", border_width=2, cursor= "hand2", width=80)
save_button.place(x=10, y=255)

app.mainloop()