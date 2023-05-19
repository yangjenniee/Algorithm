import sys

while True :
        a = int(sys.stdin.readline().rstrip())

        if a == -1 :
            break
        yak=[]

        for i in range(1,a) :
            if a%i==0 :
                yak.append(i)
        if sum(yak) == a :
            print("%d = "%a,end='')
            for j in range(len(yak)-1) :
                print("%d + "%yak[j],end='')
            print(yak[-1])

        else :
            print("%d is NOT perfect."%a)

