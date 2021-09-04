# 8958
#9/4
# 질문글 참조

n=int(input())

for _ in range(n):
    test=input()
	
    score=0
    temp=1 #연속성을 위해 생긴 임시 변수
    
    for i in test:
        if i == 'O':
            score += temp
            temp += 1
	    
        else:
            temp = 1
        
    print(score)