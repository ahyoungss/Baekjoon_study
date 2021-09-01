#10952
#8/21
list_a = []
list_b = []
while True:
  a, b = map(int,input().split())
  if(a==0 and b==0):
    break
  else:
    list_a.append(a)
    list_b.append(b)

for i in range(0,len(list_a)):
  print(list_a[i]+list_b[i])
