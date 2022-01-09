Que.write python program to Armstrong Number in interval.
program:-

a=int(input("Enter Start Number"))
b=int(input("Enter End Number"))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
        n=int(n/10)
        s=s+(d*d*d)
    if(s==i):
        print(i)


output:-
Enter Start Number100
Enter End Number500
153
370
371
407