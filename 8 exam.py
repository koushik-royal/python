def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_and_composite(numbers):
    prime_count = 0
    composite_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1
    return prime_count, composite_count

# Example usage:
numbers = []
n = int(input("Enter the number of elements: "))
print("Enter the numbers:")
for i in range(n):
    num = int(input())
    numbers.append(num)

prime_count, composite_count = count_prime_and_composite(numbers)
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)
