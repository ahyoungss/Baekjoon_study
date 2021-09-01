#1546
#8/27

n = int(input())
score = list(map(int,input().split()))
sum =0
rescore = []

for i in range(n):
  rescore.append(score[i]/max(score)*100)  
  sum+=rescore[i]

print(sum/n)
