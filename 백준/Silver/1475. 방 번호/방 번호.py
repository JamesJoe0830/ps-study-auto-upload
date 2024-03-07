# https://www.acmicpc.net/problem/1475
import sys
input = sys.stdin.readline

nums=list(input().rstrip())

for i in range(len(nums)):
    nums[i] = int(nums[i])
numset = [0]*10

for i in nums:
    if i == int(6) or i == int(9):
        if numset[6] <= numset[9]:
            numset[6] += 1
        else:
            numset[9] += 1
    else:
        numset[i] +=1

print(max(numset))
