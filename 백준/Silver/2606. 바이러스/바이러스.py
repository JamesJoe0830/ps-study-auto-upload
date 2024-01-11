# https://www.acmicpc.net/problem/2606
# 2606. 바이러스 [🥈실버 3] 
# ⏰ 걸린 시간 :8분
# 
# [recursion DFS로 푼 근거]
# ✅ 재귀 함수를 돌면서 연결된 요소들을 하나로 보고 깊이 탐색이 유리
# 0. DFS 알고리즘 특성 깊이 탐색을 한다.
# 1. 해당 문제의 DFS는 바이러스 컴퓨터를 체크하는 것이다.
# 2. 깊게 탐색후 바이러스 감염을 다 체크하고 나오는 것이 목표이기 때문에 DFS가 적합하다고 판단했다.
# ---------------------------------------------------------------------------
import sys
input = sys.stdin.readline
computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]

for i in range(connect):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
cnt = 0 

def dfs(node):
    global cnt
    cnt += 1
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)
    
    return cnt

print(dfs(1)-1)