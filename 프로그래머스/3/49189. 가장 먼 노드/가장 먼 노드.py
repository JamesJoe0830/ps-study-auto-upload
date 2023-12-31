from collections import deque
def solution(n, edge):
    answer = 0
    tree = [[] for _ in range(n+1)]
    for start, end in edge:
        tree[start].append(end)
        tree[end].append(start)
    Q = deque()
    lengths = [0 for _ in range(n+1)]
    Q.append((1,0))
    lengths[1] = -1
    while Q :
        next_node, layer = Q.popleft()
        for node in tree[next_node]:
            if lengths[node] == 0:
                Q.append((node,layer+1))
                lengths[node] = layer+1
    max_length = max(lengths)
    for length in lengths:
        if max_length == length:
            answer +=1
        
    
        
        
        
    return answer