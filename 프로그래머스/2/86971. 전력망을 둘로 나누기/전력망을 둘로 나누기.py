# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 86971. 전력망을 둘로 나누기 [🥈 LEVEL 2] 
# 📚 알고리즘 분류: BFS&DFS + 완전탐색 🔥 오답 필요 (시간복잡도를 줄일 수 있는 아이디어를 고민해볼 여지가 있다.)
# ⏰ 걸린 시간 : 50분
# 
# [문제 풀이]
# 0. wires의 각 연결선을 끊었을때 상황마다 dfs로 전령망 개수의 차이를 구한다.
# 1. nums에 각 연결된 정보를 저장하고
# 2. visited를 만들어 방문한 여부를 처리한다.
# 3. 하나의 전력망에 몇개의 노드가 포함되어 있는지 cnt를 통해서 계산한다.
# ------------------------------------------------------------

def solution(n, wires):
    answer = 10000

    def dfs(n):
        cnt = 1
        visited.add(n)
        for next_node in nums[n]:
            if next_node not in visited:
                cnt += dfs(next_node)
        return cnt
    for i in range(len(wires)): # wires 개수 만큼 탐색
        nums = [[] for _ in range(n+1)] # nums: 연결되어있는 선
        visited = set()
        for j in range(len(wires)):
            if i != j :   # i 번째 연결을 없앴다고 가정하기 위한 조건이다.
                nums[wires[j][0]].append(wires[j][1])
                nums[wires[j][1]].append(wires[j][0])

        dfs_call = [] #dfs_call이 일어나고 연결된 node를 저장함
        for k in range(1,n+1):
            if k not in visited:
                cnt =1 
                dfs_call.append(dfs(k))

        if len(dfs_call) == 2:
            answer = min(abs(dfs_call[0]-dfs_call[1]),answer)

    return answer
# ------------------------------------------------------------
