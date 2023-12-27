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
                print("heap",heap)
                if second[0] == "-":
                    heapify(heap)
                    a= heappop(heap)
                    print("min",a)
                else:
                    heap = [-1* n for n in heap]
                    heapify(heap)
                    # print("heap*-1",heap)
                    e=heappop(heap)
                    print("max",e)
                    heap = [-1*n for n in heap]
    print(heap)
    if heap:
        answer = [max(heap),min(heap)]
    else:
        answer = [0,0]
    
    
        
    return answer