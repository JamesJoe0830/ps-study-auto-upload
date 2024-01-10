# https://www.acmicpc.net/problem/1260
# 1260. DFS와 BFS [🥈 실버2]
# 📚 알고리즘 분류: DFS&BFS
# ⏰ 걸린 시간 : 7분
# 
# [문제 풀이]
# 1. DFS는 recursion(재귀로) stack의 개념으로 접근한다.
# 2. BFS는 Que를 통해서 계속 같은 layer는 넣어주기 때문에 Que로 접근한다.
# ----------------------------------------------------------------------- 

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    start ,end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1
visited = []
Q = deque()

# recursion DFS [깊이우선탐색]
def DFS(node):
    visited.append(node)
    for i in range(N+1):
        if graph[node][i] == 1 and i not in visited:
            DFS(i)
    return visited

# BFS [너비우선탐색]
def BFS(n):
    Q.append(n)
    visited.append(n)
    while Q :
        node = Q.popleft()
        for next_node in range(N+1):
            if graph[node][next_node] == 1 and next_node not in visited:
                visited.append(next_node)
                Q.append(next_node)
    return visited


print(*DFS(V))
visited = []
print(*BFS(V))

# ----------------------------------------------------------------------- 
