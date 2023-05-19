import sys

n=int(sys.stdin.readline().rstrip())
quater = 0
dime=0
nick=0
penn=0
a=[0,0,0,0]
for _ in range(n) :
    cost = int(sys.stdin.readline().rstrip())
    cost*=0.01
    #쿼터 구하기
    quater=cost//0.25
    cost -= quater*0.25
    cost=round(cost,2)
    a[0] = int(quater)
    #다임 구하기
    dime = cost//0.10
    cost-= dime*0.10
    cost=round(cost,2)
    a[1]= int(dime)
    #니켈 구하기
    nick = cost//0.05
    cost-= nick*0.05
    a[2] = int(nick)
    cost=round(cost,2)
    #페니 구하기
    penn = cost//0.00999
    cost-=penn*0.01
    cost = round(cost, 2)
    a[3]=int(penn)

    for aa in a :
        print(aa,end=' ')



