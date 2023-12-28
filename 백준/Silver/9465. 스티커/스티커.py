# https://www.acmicpc.net/problem/9465
# 9465. 스티커 [🥈 실버1]
# 📚 알고리즘 분류: DP 
# 🔥오답 필요 : 시간초과 및 논리 생각 못함
# ⏰ 걸린 시간 : 43분
# 시간 복잡도 : O(n) 
# [문제 풀이]
# 0. 지그재그가 아니다.
# ---------------------------------------------
import sys
input = sys.stdin.readline
T = int(input())

for tc in range(T):
    dp = []
    n = int(input())
    for i in range(2):
        row = list(map(int,input().split()))
        dp.append(row)
    if n > 1:     
        #dp[y][x]
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2]) # 다른 행에서 이전 값 두개 중에 큰값을 더해온다.
        dp[1][i] += max(dp[0][i-1],dp[0][i-2]) # 다른 행에서 이전 값 두개 중에 큰값을 더해온다.
    print(max(dp[0][n-1], dp[1][n-1]))
# ---------------------------------------------