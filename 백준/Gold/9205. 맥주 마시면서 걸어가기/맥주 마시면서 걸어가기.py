# https://www.acmicpc.net/problem/9205
# 9205. 맥주 마시면서 걸어가기  [🥇 골드 5]
# 📚 알고리즘 분류: 큐 (Que)
# ⏰ 걸린 시간 : 20분
# [문제 풀이 방법]
# 0. BFS로 접근해서 푼다.
# 1. Q에 (home_x,home_y)를 넣고 시작한다.
# 2. "편의점에 도착하면 맥주 20개로 리셋"은 사실상 무의미하다. q에서 1000(20개*50m) 보다 작다면
# 3. 바로바로 bfs탐색을 해서 now_x,now_y를 업데이트 해주기 때문에 
# 4. while문에서 목적지의 x, y값과 festival의 x, y값의 차이를 계산해서 합한 값이 1000보다 작다면 도달할 수 있는다는 것이고 이를 확인해주면 된다.
# --------------------------------------------------------------------------------------------------------------------

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    answer = "sad"
    visited = set()
    store = int(input())
    home_x, home_y = map(int,input().split())
    q = deque()
    store_q = deque()
    q.append((home_x,home_y))

    for i in range(store):
        store_x,store_y = map(int,input().split())
        store_q.append((store_x,store_y))
    festival_x,festival_y = map(int,input().split())
    while q:
        now_x,now_y = q.popleft()
        # 현재 시점이 목적지에 바로 갈 수 있는 거리라면 바로 happy 출력
        if abs(festival_x - now_x) + abs(festival_y - now_y) <= 1000: 
            answer = "happy"
            break
        if store_q:
            for i in range(len(store_q)):
                next_x = store_q[i][0]
                next_y = store_q[i][1]
                if abs(next_x - now_x) + abs(next_y - now_y) <= 1000 and i not in visited:
                    visited.add(i)
                    q.append((next_x,next_y))
    print(answer)

# --------------------------------------------------------------------------------------------------------------------
