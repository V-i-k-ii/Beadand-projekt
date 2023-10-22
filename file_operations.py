#Saját modul
def save_data_to_file(name, username, email, password):
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}\nUsername: {username}\nEmail: {email}\nPassword: {password}\n")

def load_data_from_file():
    data = []
    try:
        with open("user_data.txt", "r") as file:
            lines = file.readlines()
            name = ""
            username = ""
            email = ""
            password = ""
            for line in lines:
                if line.startswith("Name: "):
                    name = line.strip().split(": ")[1]
                elif line.startswith("Username: "):
                    username = line.strip().split(": ")[1]
                elif line.startswith("E-mail: "):
                    email = line.strip().split(": ")[1]
                elif line.startswith("Password: "):
                    password = line.strip().split(": ")[1]
                    data.append((name, username, email, password))
        return data
    except FileNotFoundError:
        return []