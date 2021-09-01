#10818
#8/25

n = int(input())
data = list(map(int,input().split()))
data.sort()

print(data[0],data[n-1])
