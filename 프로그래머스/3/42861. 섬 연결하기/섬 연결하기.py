# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# MST(최소 신장 트리) 알고리즘 프림 이용해야한다..
# 모든 노드를 탐색하면서 가장 최소의 길이를 지나려고 하고 있다.
# prim은 시작 노드에서 시작해서 최소 간선을 추가하는 방식으로 동작한다.
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