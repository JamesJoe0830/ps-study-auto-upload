# https://www.acmicpc.net/problem/2563
# 2563. 색종이 [🥈 실버 5]
# 📚 알고리즘 분류: 구현(Implement)
# ⏰ 걸린 시간 : 21분
# 
# [문제 핵심 포인트]
# 0. 결국엔 모든 최소 길이들 배열에서 최대 길이를 끊어 마을을 나눠주면 된다.
# 
# -------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
graph = [[0]* 100 for _ in range(100)]
answer = 0

for _ in range(N):
  x, y = map(int,input().split())
  for i in range(y, y+10):
    for j in range(x, x+10):
      graph[i][j] = 1

for i in range(100):
  for j in range(100):
    if graph[i][j] == 1:
      answer += 1
print(answer)

# -------------------------------------------------------------------------------------