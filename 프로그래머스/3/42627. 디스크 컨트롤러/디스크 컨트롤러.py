# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 42627. 이중우선순위큐 [🥈 LEVEL3]
# 📚 알고리즘 분류: heapq(힙) 
# 🔥 오답 필요(시간초과 및 논리 생각 부족)
# ⏰ 걸린 시간 : 2시간 (풀이 봄)
# 시간 복잡도 : O(nlogn)
# 
# [왜 heapq로 풀어야하는가?]
# 0. 시간 효율성 : 힙을 사용하면 최소값을 빠르게 찾을 수 있으므로 O(log n)시간 복잡도가 걸린다.
# 1. 공간 효율성 : 힙은 메모리 공간을 동적 배열에 비해 메모리 소비가 적다.
# 2. 정렬된 순서 유지 : 힙은 정렬된 순서를 지속적으로 유지해준다.
# [주의사항]
# 0. 현재 시점에 결국 작업 시간이 짧은 순서대로 시행되어야 한다.
# 
# ---------------------------------------------------------------------------------

from heapq import heapify, heappop, heappush
def solution(jobs):
    answer, now = 0, 0
    length = len(jobs)
    start = -1 # 이전에 완료한 작업 시간
    heap = []
    cnt = 0 # 처리된 작업의 개수
    
    while cnt < len(jobs) : 
        # print("now",now)
        # 현재 시점에서 처리할 수 있는 작업들을 저장한다.
        for j in jobs : 
            if start < j[0] <= now: # 🔥이전에 완료한 작업 시간 ~ 현재 시점에서 처리할 수 있는 작업
                heappush(heap, [j[1],j[0]])
        # 힙에 값이 존재할때 뽑아서 현재 시간과
        if heap : 
            current = heappop(heap)
            start =now
            now += current[0] # 현재 시간에 실행시간 더해주고
            answer += now - current[1] #총 소요된 시간은 시작 시간을 현재 시간에서 빼준다.
            cnt+=1 #작업이 완료된 것의 개수를 더해준다
        else: # 처리할 작업이 없다면 시간은 흐른다.
            now +=1 
        
    return answer //length

# ---------------------------------------------------------------------------------