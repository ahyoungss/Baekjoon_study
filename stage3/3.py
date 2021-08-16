#15552
#8/16
import sys

input =sys.stdin.readline

n=int(input())
sum=[]
for i in range(0,n):
  a,b=map(int,input().split())
  sum.append(a+b)

for i in range(0,n):
  print(sum[i])

