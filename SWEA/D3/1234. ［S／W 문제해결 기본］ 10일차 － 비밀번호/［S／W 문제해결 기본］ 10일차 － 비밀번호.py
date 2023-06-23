#
T = 10
for test_case in range(1, T + 1):
   n,password = input().split()
   n = int(n)
   stk = []
   for c in password :
       if stk and c == stk[-1] :
           stk.pop()
       else : 
           stk.append(c)
           
   result = ''.join(stk)
   print(f'#{test_case} {result}')