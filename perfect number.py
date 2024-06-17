n = int(input("enter a number."))
x=n
sum =0
for i in range(1,n):
    if(n%i==0):
        sum = sum+i
if(x==sum):
    print(" is perfect number.")
else:
    print(" is not perfect number")
    
