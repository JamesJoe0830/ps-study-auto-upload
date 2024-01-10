# https://www.acmicpc.net/problem/15649
# 15649. N과 M (1) [🥈 실버3] 🔥 오답 필요
# 📚 알고리즘 분류: 백트래킹 [backtracking]
# ⏰ 걸린 시간 : 30분
# 
# [문제 풀이]
# 1. 순회하면서 backtracking을 돌면서 바로 M의 길이 만큼이라면 출력한다.
# -----------------------------------------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
visited = []
def backtracking():
    if len(visited) == M:
        print(" ".join(map(str,visited)))
        return
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            backtracking()
            visited.pop()
backtracking()




# [문제 풀이]
# 1. 노드 하나 잡고 들어간다.
# 2. 백트래킹 : visited배열에 추가하고 backtraking 접근한 후 바로 pop해줘서 원래 상태로 만들어줌
# 3. 이때 visited 길이가 M이라면 얕은 복사를 통해서 dictionary에 추가한다.
# 4. 얕은 복사를 하지 않으면 문제가 발생할 수 있다.
# [시간 초과]---------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline
# N , M = map(int,input().split())
# 
# dictionary = [] # 방문 체크
# nums = [] # 사용할 수 있는 번호들

# # 방문 node가 있을때 하나 잡고 들어가서 1 2 

# for i in range(1,N+1):
#     nums.append(i)


# def backtracking(visited):
#     if len(visited) == M :
#         if visited not in dictionary:
#             dictionary.append(visited.copy())
#             # 🔥 오답 필요
#             # copy() 를 통해 얕은 복사를 해줘야한다.
#             # 얕은 복사를 하지 않으면 하나의 visited가 바뀌면 다른 호출 스택에서도 같은 변경이 반영되어
#             # 이전 상태로 돌아갈 수 없다.
#     for next in nums:
#         if next not in visited:
#             visited.append(next)
#             backtracking(visited)
#             visited.pop() #backtracking


# for i in range(1,N+1):
#     backtracking([i])

# dictionary.sort()
# for i in range (len(dictionary)):
#     print(*dictionary[i])

# [permutations 를 이용한 풀이]-----------------------------------------------------------------------------
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
visited =[]
for i in range(1, N+1):
    nums.append(i)
visited.extend(list(permutations(nums,M)))

for permu in visited:
    print(* permu)
