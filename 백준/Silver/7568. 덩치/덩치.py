# https://www.acmicpc.net/problem/7568
# 7568. 덩치 [🥈 실버5]
# 📚 알고리즘 분류: 브루트 포스 [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 5분
# 시간복잡도 : O(N^2)
# [문제 풀이]
# 0. 몸무게, 키 모두 작다면 순위를 하나씩 증가해준다.
# ----------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
people = []
for i in range(N):
    w, l = map(int, input().split())
    people.append((w,l))
answer = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank +=1
        
    answer.append(rank)
print(*answer)
# ----------------------------------------------------------------
