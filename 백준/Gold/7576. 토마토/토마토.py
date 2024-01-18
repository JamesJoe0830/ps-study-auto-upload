# https://www.acmicpc.net/problem/7576
# 7576. 토마토 [🥇 골드 5] 
# 📚 알고리즘 분류 : BFS&DFS (by BFS)
# ⏰ 걸린 시간 : 15분
#
# [공간 효율성] : visited 필요 없다!
# 0. 바로 graph에 layer에 대한 가중치를 더해주면 된다.
# 
# 
# [BFS 알고리즘로 푼 근거 및 회고]
# ✅ 날짜가 익어가는 정도 즉, Layer를 탐색하는 것이다. -> BFS에 적합하다.
# 0. 토마토는 1인 것에서 부터 익는것을 결정한다. 1이 여러개 일때 익는 시점(날짜)는 0으로 같다. 
# 1. Queue에 1인것 모두 다 넣고 Que를 빼주면서 시작하면 된다.
# 2. BFS를 돌고 마지막에 0 이 남아있다면 익지 못한 것이라서 -1을 출력
# --------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int,input().split())
box = [] 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()
for i in range(N):
    box.append(list(map(int,input().split())))
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            q.append((y,x))
while q:
    cur_y, cur_x = q.popleft()

    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if 0 <= next_y < N and 0 <= next_x <M and box[next_y][next_x] == 0:
            box[next_y][next_x] = box[cur_y][cur_x] + 1
            q.append((next_y,next_x))

day = -1
ripe = True #익은지 안익었는지
for y in range(N):
    if 0 in box[y]:
        ripe = False
        break
    if max(box[y]) > day:
        day = max(box[y])
if ripe == False:
    print(-1)
else :
    print(day-1)
# --------------------------------------------------------------------
    



