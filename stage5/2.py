#2563
#8/25

data = []
for i in range(0,9):
  data.append(int(input()))

max = data[0]
max_num = 0
for i in range(0,9):
  if max < data[i]:
    max = data[i]
    max_num = i

print(max)
print(max_num+1)

#a = []
#for i in range(9):
#    a.append(int(input())
#print(max(a))
#print(a.index(max(a))+1)