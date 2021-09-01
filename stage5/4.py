#3052
#8/27
num = []

for i in range(0,10):
  num.append(int(input())%42)

num=set(num)
print(len(num))