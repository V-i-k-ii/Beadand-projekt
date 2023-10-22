#Saját modul
def save_data_to_file(name, age):
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}\nAge: {age}\n")

def load_data_from_file():
    data = []
    try:
        with open("user_data.txt", "r") as file:
            lines = file.readlines()
            name = ""
            age = ""
            for line in lines:
                if line.startswith("Name: "):
                    name = line.strip().split(": ")[1]
                elif line.startswith("Age: "):
                    age = line.strip().split(": ")[1]
                    data.append((name, age))
        return data
    except FileNotFoundError:
        return []

