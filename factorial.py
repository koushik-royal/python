def factorial(n):
    if n < 0:
        return "factorial is not defiend negative numbeer"
    elif n == 0:
        return 1
    else:
        return  n * factorial(n-1)
number=int(input("enter the number:"))
print("factorial of",number,"is:",factorial(number))
