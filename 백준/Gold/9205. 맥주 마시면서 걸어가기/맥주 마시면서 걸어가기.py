# https://www.acmicpc.net/problem/9205
# 
# 
# 
# 편의점, 상근이네 집, 펜타포트 락 페티벌
# 편의점에 도착하면 맥주 20개로 리셋

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
        if abs(festival_x - now_x) + abs(festival_y - now_y) <= 1000:
            answer = "happy"
            break
        if store_q:
            for i in range(len(store_q)):
                next_x = store_q[i][0]
                next_y = store_q[i][1]
                # print(next_x != now_x and next_y!=now_y and (next_x - now_x) + (next_y - now_y) <= 1000)
                if abs(next_x - now_x) + abs(next_y - now_y) <= 1000 and i not in visited:
                    visited.add(i)
                    q.append((next_x,next_y))
    print(answer)