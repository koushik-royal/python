n = int(input("entern a number:"))
rem=0
rev=0
x=n
while n != 0:
    rem = n%10
    rev=rev+rem**3
    n//=10
if x==rev:
    print(x,"is an Armstrong number")
else:
    print(x,"is not")
