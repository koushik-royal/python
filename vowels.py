def are_vowels_concent(string):
    vowels = set("aeiouAEIOU")  
    for char in string:
        if char not in vowels:
            return False
    return True
test_string = input("Enter a string: ")
if are_vowels_concent(test_string):
    print("The string contains only vowels.")
else:
    print("The string does not contain only vowels.")
