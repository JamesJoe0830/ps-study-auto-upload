# https://www.acmicpc.net/problem/1926
# 1926. 그림 [🥈 실버 1]
# 📚 알고리즘 분류 : BFS&DFS (by recursive DFS)
# ⏰ 걸린 시간 : 7분
#
# 
# [recursive DFS 알고리즘로 푼 근거 및 회고]
# ✅ 범위를 탐색하면서 그림의 개수와 가장 넓은 값을 출력한다.
# 0. DFS를 들어갈때마다 그림의 수(picture)는 1씩 증가한다.
# 1. recursive를 돌때마다 넓이(area)는 1씩 증가한다. max값을 계속 업데이트해준다.
# --------------------------------------------------------------------

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m =map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# recursive DFS
def dfs(y,x):
    global area
    area += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx]:
            graph[ny][nx] = 0
            
            dfs(ny,nx)
    return max(max_area,area)

picture = 0
max_area = 0

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            area = 0
            picture += 1
            graph[y][x] = 0
            max_area = dfs(y,x)
print(picture)
print(max_area)
# --------------------------------------------------------------------