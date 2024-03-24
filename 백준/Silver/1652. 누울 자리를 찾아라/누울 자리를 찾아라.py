# https://www.acmicpc.net/problem/1652
# 1652. 누울 자리를 찾아라 [🥈 실버 5]
# 📚 알고리즘 분류: 구현 (Implementation -> DFS로 해결)
# ⏰ 걸린 시간 : 26분
# 
# [문제 핵심 포인트]
# 0. 깊은 복사를 통해 두개의 그래프를 놓고
# 1. 하나는 'x 방향 오른쪽'으로 나아가고 , 다른 하나는 'y 방향 아래쪽'으로 나아간다.
# 2. 이렇게 했을때 각각의 cnt 값을 리턴해서 1보다 크다면 width or height 를 더해주면 된다.
# 
# -------------------------------------------------------------------------------------

import sys, copy
input = sys.stdin.readline
N = int(input())
wgraph = []

for i in range(N):
  row = list(input().rstrip())
  wgraph.append(row)
hgraph= copy.deepcopy(wgraph)
dx = [0,1]
dy = [1,0]
width = 0
height = 0
def dfs(direction, y,x,graph, cnt):
  graph[y][x] = 'X'
  if direction == 'w':
    cnt =1
    if 0<=x+1<N and graph[y][x+1] == '.':
      cnt += dfs('w', y, x+1,graph,cnt)
  elif direction == 'h':
    cnt =1
    if 0<=y+1<N and graph[y+1][x] == '.':
      cnt += dfs('h', y+1,x,graph,cnt)
  return cnt


for i in range(N):
  
  for j in range(N):
    if wgraph[i][j] == '.':
      cnt = 1
      # print("가로:",dfs('w',i,j,wgraph,cnt))
      if (dfs('w',i,j,wgraph,cnt)) > 1:
        width += 1
    if hgraph[i][j] == '.':
      hcnt = 1
      # print("세로:",dfs('h',i,j,hgraph,hcnt))
      if (dfs('h',i,j,hgraph,cnt)) > 1:
        height += 1

print(width, height)

# -------------------------------------------------------------------------------------
