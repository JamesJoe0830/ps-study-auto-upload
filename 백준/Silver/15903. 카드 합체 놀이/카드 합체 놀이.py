# https://www.acmicpc.net/problem/15903
# 15903. 카드 합체 놀이 [🥈 실버 1] 
# 📚 알고리즘 분류: 힙(Heap)
# ⏰ 걸린 시간 : 5분
# 
# [문제 풀이]
# 0. 최소 힙 문제는 계속 힙의 형태가 유지되는데 시간 복잡도가 O(logN) 이렇게 되기 때문에
# 1. N이 100,000 이기 때문에 계속 정렬을 하면 시간초과가 난다.
# 2. 두개의 가장 작은 원소를 뽑고 더한 값을 2번 넣어주는 과정을 반복한다 (cnt와 M이 일치할 떄 까지)
# ----------------------------------------------------------------------------

import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline


N, M = map(int, input().split())
heap = list(map(int, input().split()))

heapify(heap)

cnt = 0 
while cnt != M:
    x = heappop(heap)
    y = heappop(heap)
    new = x+y
    heappush(heap,new)
    heappush(heap,new)
    cnt +=1
print(sum(heap))

# ----------------------------------------------------------------------------