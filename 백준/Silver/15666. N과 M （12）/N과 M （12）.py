
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

