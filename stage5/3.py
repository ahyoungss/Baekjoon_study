#2577
#8/27

a=int(input())
b=int(input())
c=int(input())

sum = str(a*b*c)

count = 0

for i in range(0,10):
  for j in sum:
    if i == int(j):
      count += 1
  print(count)
  count = 0

