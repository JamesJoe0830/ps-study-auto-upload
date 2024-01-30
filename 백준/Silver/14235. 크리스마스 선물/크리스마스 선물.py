# https://www.acmicpc.net/problem/14235
# 14235. 크리스마스 선물 [🥈 실버 3] 
# 📚 알고리즘 분류: 힙(Heap) -> 최대 힙
# ⏰ 걸린 시간 : 13분
# 
# [최대 힙 접근]
# 0. 최소 힙에서 -1 을 해주면 최대힙이 된다.
# 
# [문제 풀이]
# 0. 최소 힙 문제는 계속 힙의 형태가 유지되는데 시간 복잡도가 O(logN) 이렇게 되기 때문에
# 1. 0 일때는 선물이 있다면 선물을 주지만, 없다면 -1을 출력한다.
# 2. 여기서 최대힙을 구현하는 방법은 -1을 곱해주고 뽑았을때 다시 -1을 곱해서 뽑아주면 된다.
# ------------------------------------------------------------------------
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

N = int(input())
heap = []
heapify(heap)

for i in range(N):
    a = list(map(int,input().split()))
    if a[0] == 0 :
        if heap:
            gift = heappop(heap)
            print(-gift)
        else:
            print(-1)
    else:
        for i in range(1,len(a)):
            heappush(heap,-a[i])

# ------------------------------------------------------------------------
