#10809
#9/4

test = input()
temp = 96

for i in range(0,26):
  temp += i
  for j in range(len(test)):
    if(test[j]==chr(temp)):
      print(j)
    else: print(-1)


for i in range(len(test)):
  if test[i]==temp