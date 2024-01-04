# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

# N : 물품의 수 K: 버틸 수 있는 무게
N, K = map(int, input().split())
arr = [[0,0]]
for i in range(N):
    # W : 물건의 무게, # V: 물건의 가치
    W, V = map(int, input().split())
    arr.append((W, V))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):    
    for j in range(i,K+1):
        weight = arr[i][0]
        value = arr[i][1]

        if weight <= j:         
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][K])
