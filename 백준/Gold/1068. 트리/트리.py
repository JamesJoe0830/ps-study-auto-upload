# https://www.acmicpc.net/problem/1068
# 1068. 트리 [🥇 골드 5] (🔥 오답 필요)
# 📚 알고리즘 분류 : BFS&DFS (by recursion DFS)
# ⏰ 걸린 시간 : 43분
#
# 
# [DFS 알고리즘로 푼 근거 및 회고]
# ✅ 결국 마지막 leaf node 인지 확인하려면 깊이 우선 탐색이 좀더 적합하다.
# 0. remove_node를 dfs로 제거한다.
# 1. 제거 후 leaf노드를 탐색한다. (이때 모든 노드의 최상위 부모가 제거된 예외를 생각해야한다.)
# 2. 다음 노드의 값이 없는 leaf노드일때 leaf_node +=1 을 해준다.
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

for i in range(N):
    if relation[i] != -1:
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
    # cnt는 제거된 노드들을 계산한다. 이떄 next 노드들 중에 제거된 노드들을 빼고 leaf인지 검사
    for next in tree[node]:
        if next in remove_nodes:
            cnt -=1
    if cnt == 0: # 그 다음 노드가 없을 경우 leaf노드 다!
        leaf_node +=1
    for next in tree[node]:
        if next not in remove_nodes:
            leaf_dfs(next)

DFS(delete_node)

# ❗️ 예외처리 조심(부모노드가 제거가 됐을 수 있다!!)
if parent_node not in remove_nodes: # 부모노드가 제거된 노드가 아닐경우
    leaf_dfs(parent_node)
    print(leaf_node)
else:                               # 부모노드가 제거된 노드라면 0이 출력
    print(0)








# # ------------------------------------------------------------
# 풀이 설명
# 1. 입력된 인덱스를 dfs함수에 트리 배열과 함께 전달한다.

# 2. dfs함수

#   2-1. 전달받은 인덱스의 배열 값을 삭제한다는 의미로 -2로 바꾼다. (-1은 루트노드와 겹치므로 피한다.)

#   2-2. 배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs함수를 재귀호출한다.

# 3. 재귀가 끝나면 삭제될 노드들은 전부 -2로 갱신되어있으므로,

#    -2가 아니면서, 다른 노드의 부모노드도 아닌 원소를 찾을 때마다 count를 1씩 늘린다.

import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)
