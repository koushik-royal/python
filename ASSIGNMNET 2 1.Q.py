from itertools import product

def generate_combinations(d):
    letter_lists = list(d.values())
    
    combinations = product(*letter_lists)
    
    combinations = [''.join(comb) for comb in combinations]
    
    return combinations

letter_dict = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
    '3': ['e', 'f']
}
combinations = generate_combinations(letter_dict)
for comb in combinations:
    print(comb)
