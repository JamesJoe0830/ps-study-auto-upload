# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 1647. 도시 분할 계획 [LEVEL 3]
# 📚 알고리즘 분류: MST (최소 스패닝 트리) [Kruskal 알고리즘, Prim 알고리즘]
# ⏰ 걸린 시간 : 28분
# 
# [최소 스패닝 트리 알고리즘 푼 근거 및 회고]
# MST(최소 신장 트리) 알고리즘을 사용해야한다. => 모든 node가 연결되어 있고, 최소 연결 거리를 찾고자 한다.
# 0. 모든 노드를 탐색하면서 가장 최소의 길이를 지나려고 하고 있다.
# 1. 사이클이 없다.
# 📚 [Prim]
# prim은 시작 노드에서 시작해서 최소 간선을 추가하는 방식으로 동작한다.
# 0. 임의의 시작 정점을 선택
# 1. 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
# 2. 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
# 비슷한 알고리즘으로 다익스트라 알고리즘이 있다.
# 🍯 다익스트라는 전체 요소를 연결하는 것이 아닌 한 정점에서 다른 정점으로 가는 가장 짧은 방법을 구할 때 사용한다.
# ------------------------------------------------------------------------------------
import heapq

def solution(n, costs):
    answer = 10**9
    roots = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    now = 0

    for start,end,cost in costs:
        roots[start].append((cost,end))
        roots[end].append((cost,start))
    print("roots",roots)
    def prim():
        q=[]
        q.append((0,0))
        total_cost = 0
        while q : 
            print("q",q)
            print("node_cost",total_cost)
            cost, node = heapq.heappop(q)
            if visited[node] == 0 :
                visited[node] = 1
                total_cost += cost
                for next_cost, next_node in roots[node] :
                    heapq.heappush(q,(next_cost, next_node))
        return total_cost

    return prim()
# ------------------------------------------------------------------------------------
