#11021
#8/16

n = int(input())

sum=[]
for i in range(0,n):
  a,b = map(int,input().split())
  sum.append(a+b)

for i in range(0,n):
  print("Case #%d:"%(i+1),sum[i])