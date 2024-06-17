def count_vowels_and_consonants(statement):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    num_vowels = 0
    num_consonants = 0
    
    for char in statement:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
    
    print(f"Number of vowels = {num_vowels}")
    print(f"Number of consonants = {num_consonants}")
    
    if num_vowels > num_consonants:
        print("Vowels are more.")
    elif num_consonants > num_vowels:
        print("Consonants are more.")
    else:
        print("Both vowels and consonants are equal.")

# Sample Input
statement = "Saveetha School of Engineering"

# Run the function with the sample input
count_vowels_and_consonants(statement)
