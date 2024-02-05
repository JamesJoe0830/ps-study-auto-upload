# https://www.acmicpc.net/problem/11000
# 11000. 강의실 배정 [🥇 골드 5] 
# 📚 알고리즘 분류: 힙(Heap)
# ⏰ 걸린 시간 : 15분
# 
# [문제 풀이]
# 0. 최소 힙 문제는 계속 힙의 형태가 유지되는데 시간 복잡도가 O(logN) 이렇게 되기 때문에
# 1. N이 100,000 이기 때문에 계속 정렬을 하면 시간초과가 난다.
# 2. 끝나는 시간이 시작시간보다 새로운 강의실느낌으로 하나 더 넣어준다.
# 3. 만일 heap의 첫번째 요소 즉, 끝나는 시간이 시작시간보다 크면 새로 값을 업데이트 해준다.
# ----------------------------------------------------------------------------

import sys
from heapq import heappop, heappush, heapify

N = int(input())

q = [list(map(int,input().split())) for _ in range(N)]
q.sort()

heap = []
heappush(heap, q[0][1])

for i in range(1,N):
    if q[i][0] < heap[0]:
        heappush(heap, q[i][1])
    else:
        heappop(heap)
        heappush(heap, q[i][1])
print(len(heap))

# ----------------------------------------------------------------------------