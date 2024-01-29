# https://www.acmicpc.net/problem/1927
# 1927. 최소 힙 [🥈 실버 2] 
# 📚 알고리즘 분류: 힙(Heap)
# ⏰ 걸린 시간 : 13분
# 
# [문제 풀이]
# 0. 최소 힙 문제는 계속 힙의 형태가 유지되는데 시간 복잡도가 O(logN) 이렇게 되기 때문에
# 1. N이 100,000 이기 때문에 계속 정렬을 하면 시간초과가 난다.
# -------------------------------------------------------------------

import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

N = int(input())
heap = []
heapify(heap)
for i in range(N):
    a = int(input())
    if a == 0 and heap:
        pop_element = heappop(heap)
        print(pop_element)
    elif a==0 and len(heap) == 0:
        print(0)

    else:
        heappush(heap, a)

# -------------------------------------------------------------------