#for 문을 돌면서 몇개 선택할 것인지 정한다 visited에 있는지 확인한다.
# 백트래킹
# 중복된 index값을 허용하지 않는다.

def solution(elements):
    answer = 0
    visited = set()
    
    
    for i in range(len(elements)):
        ssum = elements[i]
        visited.add(ssum)
        # i 는 연속 수열 개수
        for j in range(i+1,len(elements)+i):
            ssum += elements[j%len(elements)]
            visited.add(ssum)
    
    return len(visited)