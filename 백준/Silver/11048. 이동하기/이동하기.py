# https://www.acmicpc.net/problem/11048
# 11048. 이동하기 [🥈실버 2]
# 📚 알고리즘 분류: DP
# ⏰ 걸린 시간 : 30분
# 시간 복잡도 : O(n^2) 
# [문제 풀이]
# 0. 나아갈 수 있는 방법 3가지 중에서 선택을 한다.
# 1. r,c 의 관점에서 [r-1][c], [r][c-1], [r-1][c-1]의 값을 현재값(maze[r][c])에 더하고
# 2. 셋중 가장 큰 값을 dp 에 저장한다.
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0]  = maze[0][0]

for r in range(N):
    for c in range(M):
        first, second, third = dp[r][c],dp[r][c],dp[r][c]
        if 0 <= r-1 :
            first = maze[r][c]+dp[r-1][c]
        if 0 <= c-1:
            second = maze[r][c]+dp[r][c-1]
        if 0 <= r-1 and 0 <= c-1 : 
            third = maze[r][c]+dp[r-1][c-1]
        dp[r][c] = max(first,second,third)
print(dp[N-1][M-1])
# ------------------------------------------------------------------------------