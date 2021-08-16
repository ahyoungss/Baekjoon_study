#11022
#8/16

n = int(input())

sum=[]
alist=[]
blist=[]
for i in range(0,n):
  a,b = map(int,input().split())
  sum.append(a+b)
  alist.append(a)
  blist.append(b)

#Case #1: 1 + 1 = 2
for i in range(0,n):
  print("Case #%d:"%(i+1),alist[i], "+", blist[i], "=", sum[i])