# https://www.acmicpc.net/problem/1068
# 1068. 트리 [🥇 골드 5] 
# 📚 알고리즘 분류 : BFS&DFS (by recursion DFS)
# ⏰ 걸린 시간 : 22분
#
# 
# [DFS 알고리즘로 푼 근거 및 회고]
# ✅ 결국 마지막 leaf node 인지 확인하려면 깊이 우선 탐색이 좀더 적합하다.
# 0. remove
# --------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
relation = list(map(int,input().split()))
tree = [[] for i in range(N)]
delete_node = int(input())
remove_nodes = set()
remove_nodes.add(delete_node)
leaf_node = 0 
parent_node = -1
# [[1,2],[3,4],[],[],[]]
for i in range(N):
    if relation[i] != -1:
        # print(relation[i])
        tree[relation[i]].append(i)
    else:
        parent_node = i
# tree
def DFS(node):
    for next in tree[node]:
        if next not in remove_nodes:
            remove_nodes.add(next)
            DFS(next)
#leaf node를 찾기 위한 recursion dfs
def leaf_dfs(node):
    global leaf_node
    cnt = len(tree[node])
    for next in tree[node]:
        if next in remove_nodes:
            cnt -=1
    if cnt == 0: # 그 다음 노드가 없을 경우 leaf노드 다!
        leaf_node +=1
    for next in tree[node]:
        if next not in remove_nodes:
            leaf_dfs(next)

DFS(delete_node)
if parent_node not in remove_nodes:
    leaf_dfs(parent_node)
    print(leaf_node)
else:
    print(0)

