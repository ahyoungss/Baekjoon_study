#10871
#8/16

n,x = map(int,input().split())

num = list(map(int,input().split()))
answer = []
for i in range(0,n):
  if num[i] < x:
    answer.append(num[i])

print(answer)