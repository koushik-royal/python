str1=str(input("Enter string : "))
x=len(str1)
vow=0
con=0
for i in range(0,x):
    ch=str1[i]
    if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U'):
        vow=vow+1
    else:
        con=con+1
print("no of vowels are : ",vow)
print("no of consonants are : ",con)
if(vow>con):
    print("vowels are maximun")
elif(vow==con):
    print("Both are equal")
else:
    print("consonants are maximum")
