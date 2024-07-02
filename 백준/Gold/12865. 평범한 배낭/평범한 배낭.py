# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline
def knapsack():
    N, K = map(int, input().split())
    arr =[]
    dp = [[0]*(K+1) for _ in range(N+1)]
    for _ in range(N):
        W, V = map(int, input().split())
        arr.append((W,V))
    for i in range(1,N+1):
        for j in range(i,K+1):
            weight = arr[i-1][0]
            value = arr[i-1][1]
    # 무게를 넘지 않으면서 최대로 만들 수 있는 가치를 측정하는 것이다.
            if j >= weight:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
            else : 
                dp[i][j] = dp[i-1][j]
    return dp[-1][K]
print(knapsack())
