# https://www.acmicpc.net/problem/1021
# 1021. 도시 분할 계획 [🥈 실버 3]
# 📚 알고리즘 분류: 큐 (Que)
# ⏰ 걸린 시간 : 20분
# 
# [풀이 방법]
# 0. 큐를 사용해서 구현한다.
# 1. 현재 뽑아야하는 노드가 앞에서 뽑는게 빠르다면 앞에서 뽑고
# 2. 뒤에서 뽑는게 빠르다면 뒤에서 뽑는다.
# ------------------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
pop_num = list(map(int,input().split())) #뽑는 번호 정렬 
pop_num = deque(pop_num)
q = deque()
answer = 0 

# 값 넣기
for i in range(1,N+1):
    q.append(i)

# q
while pop_num :
    if q:
         #현재 index의 값이 앞보다 뒤의 길이가 더 클경우
        if q.index(pop_num[0]) < len(q)-q.index(pop_num[0]):
            value = q.popleft()
            if value != pop_num[0]:
                q.append(value)
                answer +=1
            elif value == pop_num[0]:
                pop_num.popleft()

        else:
            value = q.pop()
            q.appendleft(value)
            answer +=1
print(answer)
# ------------------------------------------------------------------------------------
            