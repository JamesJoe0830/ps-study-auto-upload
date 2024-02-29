import sys
import heapq
input=sys.stdin.readline

V, E = map(int,input().split())

graph =[[] for _ in range(V+1)]
visited=[0 for _ in range(V+1)]


for i in range(E):
    A,B,C = map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

def prim():
    q = []
    answer,cnt = 0, 0
    q.append((0,1))
    while q:
        if cnt ==V:
            break

        len, node = heapq.heappop(q)
        if visited[node] == 0:
            visited[node] = 1
            answer += len
            cnt+=1
            for next_len, next_node in graph[node]:
                heapq.heappush(q, (next_len,next_node))
    return print(answer)
prim()