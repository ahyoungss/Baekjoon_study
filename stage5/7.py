#4344
# 8/29

n = int(input())
sum = 0
count = 0

for i in range(n):
  case = list(map(int,input().split()))
  for j in range(case[0]):
    sum += case[j+1]
  average = sum/case[0]
  for j in range(case[0]):
    if case[j+1] > average:
      count += 1
  print("%.3f%",count/case[0])