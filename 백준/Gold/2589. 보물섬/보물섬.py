# https://www.acmicpc.net/problem/2589
# 2589. 보물섬 [🥇 골드 5] 
# 📚 알고리즘 분류 : BFS&DFS (by BFS)
# ⏰ 걸린 시간 : 25분
#
# 
# [BFS 알고리즘로 푼 근거 및 회고]
# ✅ layer의 문제이다. 얼마나 간 거리를 측정하는 것이고 같은 layer들을 함께 보기 때문에 사용함
# 0. 'L'값의 좌표 y,x를 갖고 탐색을 시작한다. distance 배열은 매 좌표마다 초기화를 해준다.
# 1. 이유는 하나의 좌표에서 갖고 가장 긴 시간이 걸리는 육지 두 곳을 확인하고 싶다.
# 2. answer은 하나의 좌표에서 생긴 거리 중 가장 긴 시간이 걸리는 값을 업데이트 해준다.
# --------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

Y, X = map(int,input().split())
graph = [list(input().rstrip()) for i in range(Y)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(y,x):
    global Y, X, answer
    Q = deque()
    Q.append((y,x))
    distance[y][x] = 0
    
    while Q :
        y,x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < Y and 0 <= nx < X and graph[ny][nx] == 'L'and distance[ny][nx] == -1 :
                distance[ny][nx] = distance[y][x] + 1
                answer = max(answer, distance[ny][nx]) # 정답 업데이트 가장 큰 값이 최종 이동경로
                Q.append((ny,nx))
    return answer

# L인 y,x 좌표 한개 잡고 BFS 탐색후 answer에 가장 큰 값이 결국 최단 거리 이동이다!
answer = 0 # 가장 긴시간이 걸리는 거리를 담는 변수
for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            distance = [[-1]*X for i in range(Y)]
            bfs(y,x)

print(answer)