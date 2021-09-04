#11720
#9/4

n=int(input())

case = list(map(int,input()))
sum=0

for i in range(len(case)):
  sum += case[i]
print(sum)