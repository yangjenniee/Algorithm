import sys
import math

a,b,v = map(int,sys.stdin.readline().rstrip().split())
result = math.ceil((v-a)/(a-b))
print(result+1)













