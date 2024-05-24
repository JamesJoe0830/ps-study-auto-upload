def solution(want, number, discount):
    answer = 0
    needs = {want[i]:number[i] for i in range(len(want))}
    index = 0
    while index + 10 <= len(discount) :
        current_needs = needs.copy()

        for i in range(index,index+10):
            if discount[i] in current_needs.keys() and current_needs[discount[i]] > 0:
                current_needs[discount[i]] -= 1
        if sum(current_needs.values()) == 0 :
            answer += + 1
        index += 1
        
    return answer