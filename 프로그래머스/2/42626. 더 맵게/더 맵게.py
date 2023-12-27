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