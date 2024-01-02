# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 43163. 단어 변환 [🥈 LEVEL 2]
# 📚 알고리즘 분류: Greedy -> 큐(Que)를 이용함
# ⏰ 걸린 시간 : 40분
# 
# [풀이 방법]
# 0. Q를 사용해서 list의 효율성을 높인다.
# 1. 값을 오름차순으로 정렬해서 현재 상황에서 최소와 최대 값을 볼 수 있도록 만든다. nlogn
# 2. Q의 길이가 2이상일때, 최소값 + 최대값 <= limit 일때 하나의 보트에 타고 answer -= 1 해준다.
# 3. 그 외에는 최대값 때문에 조건을 만족하지 못하는 경우라서 계속 최대값 빼준다. Q.pop()
# ---------------------------------------------------------------------
from collections import deque
def solution(people, limit):
    answer = len(people)
    people.sort() 
    Q = deque(people)
    while Q :
        if len(Q)>1 and Q[0] + Q[-1] <= limit:
            Q.pop()
            Q.popleft()
            answer -= 1
        else: 
            Q.pop()
    
        # 아래 코드는 시간초과 
        # 이유 : remove의 시간복잡도 O(N)
        # ----------------------------
        # weight = Q.popleft()
        # end -=1
        # for i in range(end, -1, -1):
        #     if weight + Q[i] <= limit:
        #         Q.remove(Q[i])
        #         end = i
        #         answer-=1
        #         end-=1
        #         break

    return answer
# ---------------------------------------------------------------------