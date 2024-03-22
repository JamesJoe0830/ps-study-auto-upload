from collections import deque 

def solution(maps):
    answer = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque()
    q.append((0,0))
    find = False
    # m = y길이 , n = x길이
    m = len(maps)-1
    n = len(maps[0])-1
    
    #BFS
    while q:
        y, x = q.popleft()
        
        if y ==m  and x == n:

            find = True
            break
        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny <= m and 0 <= nx <= n and maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        q.append((ny,nx))
    if find == True:
        answer = maps[m][n]
    else:
        answer = -1
        
        
    return answer