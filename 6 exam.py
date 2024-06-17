def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_prime(a, b):
    for num in range(a, b+1):
        if not is_prime(num):
            print(num)

a = 13
b = 19
print("Non-prime numbers between", a, "and", b, "are:")
print_non_prime(a, b)
