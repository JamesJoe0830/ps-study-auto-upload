import math
def check(i,n,answer):
    person = i % n
    if person == 0:
        person = n
    order = math.ceil(i / n)
    answer = [person, order]
    return answer
        

def solution(n, words):
    answer = [0,0] # [번호, 차례]
    visited = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in visited:
            if visited[-1][-1] == words[i][0]:
                visited.append(words[i])
            else:
                answer = check(i+1, n,answer)
                break
        else:
            answer = check(i+1, n,answer)
            break
        
        
    return answer