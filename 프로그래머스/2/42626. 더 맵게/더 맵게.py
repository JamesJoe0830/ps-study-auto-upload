# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 42626. 더 맵게 [🥈 LEVEL2]
# 📚 알고리즘 분류: Heap
# ⏰ 걸린 시간 : 28분
# 시간 복잡도 : O(nlogn)
# 
# [왜 heapq로 풀어야하는가?]
# 0. 시간 효율성 : 힙을 사용하면 최소값을 빠르게 찾을 수 있으므로 O(log n)시간 복잡도가 걸린다.
# 1. 공간 효율성 : 힙은 메모리 공간을 동적 배열에 비해 메모리 소비가 적다.
# 2. 정렬된 순서 유지 : 힙은 정렬된 순서를 지속적으로 유지해준다.
# --------------------------------------------------------------------
# 
from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    print(scoville[0],scoville[1])
    while scoville[0]<K :
        if len(scoville)==2 and scoville[0] +scoville[1] * 2 < K :
            answer = -1
            break
        first = heappop(scoville)
        second = heappop(scoville)
        answer +=1
        mix = first + second *2
        heappush(scoville, mix)
        
    return answer
# --------------------------------------------------------------------