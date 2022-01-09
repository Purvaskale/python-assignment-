Que.write python program to check prime all number in an interval.
program:-

a=int(input("Enter Start Number"))
b=int(input("Enter End Number"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
output:-

Enter Start Number1
Enter End Number20
2
3
5
7
11
13
17
19