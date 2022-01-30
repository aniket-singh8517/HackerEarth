test=int(input())
while test>0:
    g,p=map(int,input().split())
    n=int(input())
    l=[]
    for i in range(n):
        li=[int(x) for x in input().split()]
        l.append(li)
    le=0
    ri=0
    for i in range(n):
        if l[i][0]==1:
            le=le+1
        if l[i][1]==1:
            ri=ri+1
    if g>p:
        if le>ri:
            tc=g*ri+p*le
        else:
            tc=g*le+p*ri
        print(tc)
    else:
        if le>ri:
            tc=p*ri+g*le
        else:
            tc=p*le+g*ri
        print(tc)
    test=test-1