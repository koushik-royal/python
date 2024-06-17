def letter_combinations(dictionary, current_combination="", key_index=0):
    if key_index == len(dictionary):
        print(current_combination)
        return

    key = list(dictionary.keys())[key_index]
    for letter in dictionary[key]:
        letter_combinations(dictionary, current_combination + letter, key_index + 1)

# Example dictionary
dictionary = {
    '1': ['a', 'b', 'c'],
    '2': ['d', 'e', 'f'],
    '3': ['g', 'h', 'i']
}

letter_combinations(dictionary)
