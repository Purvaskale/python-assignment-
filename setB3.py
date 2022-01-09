Que.python program to check Prime number.
program:-

p=int(input("Enter no:"))
flag=0
for i in range(2,p):
    if(p%i==0):
        flag=1
if(flag==0):
    print("Number is Prime")
else:
    print("Number is Not Prime")

output:-

Enter no:23
Number is Prime