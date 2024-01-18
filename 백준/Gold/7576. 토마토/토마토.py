import sys
from collections import deque

input = sys.stdin.readline
# M: 가로칸의 개수, N: 세로칸의 개수
M, N = map(int, input().split())

graph = [list(map(int,input().split())) for i in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
Que = deque()

# M(가로 : x ):6 N(세로, y):4 
# 먼저 Que에 1인거 다 넣어주기 (익는 시점은 1이 있는게 다 동일하므로)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            Que.append((i,j))

while Que:
    (x,y) = Que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <=N-1 and 0<= ny <=M-1 :
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                Que.append((nx,ny))


day = 0
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer = -1
            break
        else:
            day = max(day,graph[i][j])

if answer != -1:
    answer = day-1
print(answer)