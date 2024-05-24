# https://school.programmers.co.kr/learn/courses/30/lessons/131127#
# 131127. 할인 행사 [🥈 LEVEL2]
# 📚 알고리즘 분류: 딕셔너리
# ⏰ 걸린 시간 : 28분
# 시간 복잡도 : O(n*m) n: want길이, m: discount 길이
# [문제 주의 사항]
# 1. 문제는 가능한 모든 날을 다 더하는 것이다. 가능한 날의 최소값을 구하는 것이 아니다.
# 
# [문제 풀이]
# 1. 딕셔너리를 활용해서 want를 key로 number를 value로 저장한다.
# 2. 이때 discount를 10일값만 순회하면서 -1씩 해주고 (단, value값이 0이상 일때)
# 3. 결국 모든 합이 0을 만족하게 되면 answer값을 1증가
# --------------------------------------------------------------------

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

# --------------------------------------------------------------------
