import math
def solution(citations):
    answer = max(citations)
    citations.sort()
    now = 0
    print(citations)
    while True:
        for i in range(len(citations)-1):
            if citations[i] <= answer < citations[i+1]:
                if citations[i] == answer:
                    now = i
                else : 
                    now = i + 1
                break
        if len(citations) - now >= answer and now <= answer:
            break
        else:
            answer -=1
            
    return answer
# [1,2,8] 
# 3
# [0,100]