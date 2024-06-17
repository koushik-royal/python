str1="saveetha school"
x=len(str1)
line=0
for i in range(0,x):
    ch=str1[i]
    if(ch=='\n'):
        line=line+1
print(line)
