# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 42628. 이중우선순위큐 [🥈 LEVEL3]
# 📚 알고리즘 분류: heapq(힙)
# ⏰ 걸린 시간 : 35분
# 시간 복잡도 : O(nlogn)
# 
# [왜 heapq로 풀어야하는가?]
# 0. 시간 효율성 : 힙을 사용하면 최소값을 빠르게 찾을 수 있으므로 O(log n)시간 복잡도가 걸린다.
# 1. 공간 효율성 : 힙은 메모리 공간을 동적 배열에 비해 메모리 소비가 적다.
# 2. 정렬된 순서 유지 : 힙은 정렬된 순서를 지속적으로 유지해준다.
# [주의사항]
# 0. 힙은 숫자들을 담고 계속해서 pop(빼낼때) 해당 값을 heapify로 최소힙 형태로 유지한다.
# 1. 최소힙으로 최대힙을 만들기 위해서 -1을 해서 pop할때 최대값을 잠깐동안 최소값 취급해서 빼낸다.
# ---------------------------------------------------------------------------------
from heapq import heappop,heapify,heappush
from collections import deque
def solution(operations):
    answer = []
    heap = []
    operations = deque(operations)
    # print(operations)
    while operations:
        order = operations.popleft()
        first, second = order.split()
        # print(first,second)
        
        if first == "I":
            heappush(heap,int(second))
        else:
            if heap:
                if second[0] == "-":
                    heapify(heap) #힙 heapify로 heap으로 만들어줌 : heappop할때 최소힙을 만들기 위해
                    a= heappop(heap)
                else: # 최대값을 빼내기 위해서 -1을 곱한다. 빼내고 다시 되돌려야한다.
                    heap = [-1* n for n in heap]
                    heapify(heap) #힙 heapify로 heap으로 만들어줌 : heappop할때 최소힙을 만들기 위해
                    e=heappop(heap)
                    heap = [-1*n for n in heap]
    # 정답 출력
    if heap:
        answer = [max(heap),min(heap)]
    else:
        answer = [0,0]
        
    return answer
# --------------------------------------------------------------------------------
