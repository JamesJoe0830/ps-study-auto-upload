# https://www.acmicpc.net/problem/15650
# 15650. N과 M (2) [🥈 실버3] 🔥 오답 필요
# 📚 알고리즘 분류: 백트래킹 [backtracking]
# ⏰ 걸린 시간 : 20분
# 
# [문제 풀이]
# 1. 순회하면서 backtracking을 돌면서 바로 M의 길이 만큼이라면 출력한다.
# 2. N 과M (1)과의 차이점은 순열과 조합에서 이 문제는 조합이라는 점이다.
# 3. for문을 num 부터 시작하면 중복을 제거할 수 있다.
# -----------------------------------------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
visited = []
def backtracking(num):
    if len(visited) == M:
        print(" ".join(map(str,visited)))
        return
    for i in range(num, N+1):
        if i not in visited:
            visited.append(i)
            backtracking(i)
            visited.pop()
backtracking(1)