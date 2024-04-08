import os
import json
from collections import Counter

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

def linear_search(sequence, number):
    """
    :param sequence:
    :param number:
    :return:
    """
    positions = []
    count = 0

    for i, num in enumerate(sequence):
        if num == number:
            positions.append(i+1)
            count += 1

    return {"positions": positions, "count": count}

def pattern_search(sequence, pattern):
    """
    :param sequence:
    :param pattern:
    :return:
    """
    positions = set()
    pattern_length = len(pattern)
    sequence_length = len(sequence)

    idx = 0

    # for i in range(sequence_length - pattern_length +1):
    #     if sequence[i:i+pattern_length] == pattern:
    #         positions.add(i)





    return positions

def main():
    # pass
    # Zavolani funkce read_data s pozadovanymi vstupy
    sequential_data = read_data("sequential.json", "unordered_numbers")

    # Vytiskni obsah promenne sequential_data
    print(sequential_data)

    number = 5
    result = linear_search(sequential_data, number)
    print(result)

    sequence = read_data("sequential.json", "dna_sequence")
    pattern = "ATA"
    result2 = pattern_search(sequence, pattern)
    print(result2)

if __name__ == '__main__':
    main()