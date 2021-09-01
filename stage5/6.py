#8958
#8/29

n = int(input())

case = []
for i in range(n):
  a = str(input())
  for j in range(len(a)):
    if a[j]='O' and a[j+1] ="O":
