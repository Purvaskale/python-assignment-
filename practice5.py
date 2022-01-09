Que.write python program to Print the fibonacci sequence.
program:-

f=0
s=1
print("Fabonnacci Series :",f,s,end="\t")
for i in range(1,15):
    t=f+s
    print(t,end="\t")
    f=s
    s=t

output:-
Fabonnacci Series : 0 1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	
