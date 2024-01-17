# https://www.acmicpc.net/problem/7562
# 7562. 나이트의 이동 [🥈 실버 1] 
# 📚 알고리즘 분류: DFS&BFS (by BFS)
# ⏰ 걸린 시간 :25분
# 
# [문제 풀이] : BFS 근거
# 1. 나이트는 결국 몇번째 만에 도달했는지 최단 거리를 구하고 싶다. -> 최소 깊이를 알고싶음
# 2. layer(계층)을 접근하는 문제는 DFS에 적합하지 않다. BFS에 적합하다.
# ----------------------------------------------------------------------- 

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for test_case in range(t):
    l = int(input())
    start_y,start_x = map(int,input().split())
    end_y, end_x = map(int,input().split())
    graph = [[0]*l for i in range(l)]
    dx = [-2,-2,2,2,-1,-1,1,1]
    dy = [1,-1,1,-1,-2,2,2,-2]
    q=deque()
    q.append((start_y,start_x,0))
    graph[start_y][start_x] = 1
    #bfs
    while q:
        cur_y,cur_x,cnt = q.popleft()
        if cur_y == end_y and cur_x == end_x:
            print(cnt)
            break
        for i in range(8):
            next_y = cur_y + dx[i]
            next_x = cur_x + dy[i]
            if 0 <= next_y < l and 0 <= next_x < l and graph[next_y][next_x] == 0:
                graph[next_y][next_x] = 1 # visited(방문체크)
                q.append((next_y, next_x,cnt+1))

# ----------------------------------------------------------------------- 
