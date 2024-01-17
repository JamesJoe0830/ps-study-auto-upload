import sys
input = sys.stdin.readline
from collections import deque
t = int(input())


dx = [-1,1,-1,1,2,-2,2,-2]
dy = [-2,-2,2,2,1,1,-1,-1]
answer = []

def BFS():
    Que.append((str_x,str_y))
    while Que:
        (x,y) = Que.popleft()
        if (end_x,end_y) == (x,y):
            answer.append(graph[x][y])
            break

        for i in range(8):
            nx_x = x + dx[i]
            nx_y = y + dy[i]
            if N > nx_x >= 0 and N > nx_y >=0 and graph[nx_x][nx_y] ==0 :
                graph[nx_x][nx_y] = graph[x][y] + 1
                Que.append((nx_x,nx_y))
            
for _ in range(t):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    str_x,str_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    graph[str_x][str_y] = 1

    Que = deque()
    BFS()



# 출력
for i in range(t):
    print(answer[i]-1)
