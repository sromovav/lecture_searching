import os
import json

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    # Nacteni povolenych klicu ze souboru
    with open("sequential.json", mode="r") as file:
        allowed_key = json.load(file)

    # Overeni, zda je zadany klic v mnozine povolenych klicu
    if field not in allowed_key:
        return None

    with open(file_name, mode="r") as f:
        data = json.load(f)

    # Vraceni hodnot
    return data.get(field)

def main():
    # pass
    # Zavolani funkce read_data s pozadovanymi vstupy
    sequential_data = read_data("sequential.json", "unordered_numbers")

    # Vytiskni obsah promenne sequential_data
    print(sequential_data)

if __name__ == '__main__':
    main()