# https://www.acmicpc.net/problem/2559
# 2559. 수열 [🥇 실버 3] 
# 📚 알고리즘 분류: 구간 합
# ⏰ 걸린 시간 : 12분 
# 
# [문제 풀이]
# 0. 구간 합을 먼저 구해놓는게 관건이다. 
# 1. N^2으로 구해버리면 시간초과가 발생하기 때문이다.
# ------------------------------------------------------------

import sys
input = sys.stdin.readline
N, K = map(int,input().split())

temp = list(map(int,input().split()))
pre_sum = sum(temp[0:K])
ans = sum(temp[0:K])
for i in range(1,N-K+1):
    pre_sum += - temp[i-1] + temp[i-1+K]
    if ans < pre_sum:
        ans = pre_sum
print(ans)
    
# ------------------------------------------------------------

# 시간초과 코드
# import sys
# input = sys.stdin.readline
# N, K = map(int,input().split())

# temp = list(map(int,input().split()))
# ans = 0
# for i in range(N-K+1):
#     if ans < sum(temp[i:i+K]):
#         ans = sum(temp[i:i+K])
# print(ans)
    
