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