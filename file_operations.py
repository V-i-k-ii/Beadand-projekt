#Saját modul
def save_data_to_file(name, age):
    with open("user_data.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}")

def load_data_from_file():
    try:
        with open("user_data.txt", "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "No data found."

