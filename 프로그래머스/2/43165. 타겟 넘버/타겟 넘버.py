# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 43165. 타겟 넘버 [🥈 LEVEL 2]
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 23분
# 
# [풀이 방법]
# 0. BFS로 접근한다.
# 1. 계층별로 접근한다. 때문에 BFS가 적합하다. 
# 2. multiple 은 [-1,1]로 해서 각각 
# ---------------------------------------------------------------------
from collections import deque
def solution(numbers, target):
    answer = 0
    multiple = [1,-1]
    layer_Q = deque()
    index = 0
    
    #초기 layer_Q 세팅
    for i in range(2):
        num = numbers[0]
        layer_Q.append((num*multiple[i],index))    
    index += 1
    
    # BFS
    while layer_Q:
        pop_value, pop_index = layer_Q.popleft()
        if pop_index == len(numbers)-1 and pop_value == target: # pop_index가 마지막 index이고 pop_value가 target일때 answer를 +1 해준다.
            answer +=1
        if pop_index+1 < len(numbers):
            for i in range(2):
                layer_Q.append((pop_value + numbers[pop_index+1]*multiple[i],pop_index+1))
                
    return answer
# ---------------------------------------------------------------------------------------
