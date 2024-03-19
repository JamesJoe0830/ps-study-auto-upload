# https://www.acmicpc.net/problem/16398
# 16398. 행성 연결 [🥇 골드 4]
# 📚 알고리즘 분류: 최소 스패닝 트리 [Kruskal 알고리즘]
# ⏰ 걸린 시간 : 24분
# 
# [문제 핵심 포인트]
# 0. 모든 행성을 연결하는데 필요한 최소비용을 출력하라. 모든 행성을 연결할 수 없는 경우는 없다.
# 
# [최소 스패닝 트리 알고리즘 푼 근거 및 회고]
# 문제 조건에서 : 모든 컴퓨터 사이에 경로가 항상 존재한다. => 모든점 연결, 최소 연결 거리
#  0. 모든 정점이 다연결 되어 있고 사이클이 없다!
#  1. Kruskal알고리즘은 간선들을 정렬해야하기 때문에 간선이 적으면 Kruskal, 많으면 Prim을 선택한다.
# 
# 📚 [Kruskal알고리즘]
# 0. 임의의 간선을 선택
# 1. 해당 간선을 잇는 정점 두개의 부모노드를 통해서 사이클 확인
# 2. 사이클을 이루지 않는다면 부모노드를 통일시킨다.
# 3. 사이클을 이루지 않기때문에 연결된 간선의 길이도 더해준다.
# -------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

# find parent 연산
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

# union parent 연산
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

N = int(input())
planets = []
parent = [0] * (N+1)
total_cost = 0

for i in range(1,N+1):
  parent[i] = i

for i in range(N):
  row = list(map(int,input().split()))
  for j in range(i+1, N):
    planets.append((row[j], i, j))
planets.sort()


for i in range(len(planets)):
  cost, x, y = planets[i]

  if find_parent(parent,x) != find_parent(parent, y):
    union_parent(parent,x,y)
    total_cost += cost
print(total_cost)

# -------------------------------------------------------------------------------------
