def save_result_to_file(result, filename):
    with open(filename, "a") as file:
        file.write(result + '\n')

def list_results_from_file(filename):
    try:
        with open(filename, "r") as file:
            results = file.read()
            return results
    except FileNotFoundError:
        return "Az eredményfájl nem található."


