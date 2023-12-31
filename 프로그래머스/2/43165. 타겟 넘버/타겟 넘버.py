# BFS로 접근한다.
# 계층별로 4, -4 => 
from collections import deque
def solution(numbers, target):
    answer = 0
    multiple = [1,-1]
    layer_Q = deque()
    index = 0
    for i in range(2):
        num = numbers[0]
        layer_Q.append((num*multiple[i],index))    
    index += 1

    while layer_Q:
        # print(layer_Q)
        pop_value, pop_index = layer_Q.popleft()
        if pop_index == len(numbers)-1 and pop_value == target:
            answer +=1
        if pop_index+1 < len(numbers):
            for i in range(2):
                layer_Q.append((pop_value + numbers[pop_index+1]*multiple[i],pop_index+1))
                
    return answer