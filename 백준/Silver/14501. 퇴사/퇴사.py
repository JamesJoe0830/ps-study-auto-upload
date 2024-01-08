# https://www.acmicpc.net/submit/14501
# 14501. 퇴사 [🥈 실버3]
# 📚 알고리즘 분류: 브루트 포스 & DP [Brute Force & DP 알고리즘]
# ⏰ 걸린 시간 : 1시간 20분
# 
# [문제 풀이]
# 1. 현재 시점 i에서 당일날 처리할 수 있는 일을 처리하고
# 2. 그 뒤 j(=i+처리기간)이후에 값들을 처리하는데.
# 3. 만약 j 시점에 일을 처리하고 난 후가 기간 내라면 j+Task[j][0] -1 <= N
# 4. dp[j]를 max값으로 업데이트한다.
# ---------------------------------------------------------------- 
import sys
input =sys.stdin.readline

N=int(input())
Task = [(0,0)]
dp = [0]*(N+1)
for i in range(N):
    # t:걸리는 기간 , p: 돈
    t, p = map(int,input().split())
    Task.append((t,p))

for i in range(1,N+1):
    if i+Task[i][0] -1 <= N :
        dp[i] = max(dp[i],Task[i][1])
        for j in range(i+Task[i][0],N+1):
            if j+Task[j][0] -1 <=N:
                dp[j] = max(dp[j],dp[i]+Task[j][1])


print(max(dp))


