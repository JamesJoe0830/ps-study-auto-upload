# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 12973. 짝지어 제거하기 [🥈 LEVEL2]
# 📚 알고리즘 분류: stack [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 10분
# 
# [문제 풀이]
# 0. 앞의 값을 차례대로 stack에 넣으면서 stack의 값과 비교해주면서 pop해주면 끝
# 
# ----------------------------------------------------------------

def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        if stack :
            if stack[-1] != s[i]:
                stack.append(s[i])
            else :
                stack.pop()
        else :
            stack.append(s[i])
    if len(stack) == 0 :
        answer = 1


    return answer

# ----------------------------------------------------------------