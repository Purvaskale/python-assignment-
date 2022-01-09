Que.python program to check  numberis Armstorng or not.
program:-

n=int(input("enter Number:"))
sum=0
n1=n
while n>0:
    d=n1%10
    n1=int(n1/10)
    sum=sum+d*d*d
if(n==sum):
    print("Number is Armstorng")
else:
    print("Number is not  Armstorng")
output:-

enter Number:153
Number is Armstorng