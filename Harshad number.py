def is_harshad_number(number):
    number_str = str(number)
    digit_sum = sum(int(digit) for digit in number_str)
    return number % digit_sum == 0
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")
