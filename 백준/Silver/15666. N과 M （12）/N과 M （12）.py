# https://www.acmicpc.net/problem/15666
# 15666. N과 M (12) [🥈 실버 2]
# 📚 알고리즘 분류: 백트래킹 [backtracking]
# ⏰ 걸린 시간 : 10분
# 
# [문제 풀이]
# 1. 순회하면서 backtracking을 돌면서 바로 M의 길이 만큼이라면 출력한다.
# 2. 단 중복은 허용하지 않기 때문에 start값을 갖고 돌고 해당 숫자부터 backtracking하게 한다.
# -----------------------------------------------------------------------
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()

visited = []
def backtracking(start):
    if len(visited) == M:
        print(" ".join(map(str,visited)))
    else:
        for next in range(start,len(nums)):
            if len(visited) != M :
                visited.append(nums[next])
                backtracking(next)
                visited.pop()

backtracking(0)

# -----------------------------------------------------------------------
