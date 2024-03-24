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
