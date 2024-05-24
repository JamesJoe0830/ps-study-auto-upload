# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 76502. 할인 행사 [🥈 LEVEL2]
# 📚 알고리즘 분류: 스택(Stack) LIFO
# ⏰ 걸린 시간 : 18분
# 시간 복잡도 : O(n*m) n: s길이 , m: check함수에서 arr 길이
# [문제 풀이]
# 1. 올바른 괄호 문제랑 똑같다. 다만 회전을 한다는 차이점이 있다는 것이다.
# 2. 회전을 하고 매번 체크해서 stack에 값이 남아 있으면 False를 리턴하도록 해서 
# 3. True를 리턴한 경우에만 answer를 증가시킨다.
# --------------------------------------------------------------------

from collections import deque
def check(arr):
    stack = [arr[0]]

    for i in range(1,len(arr)):
        if arr[i] == '[' or arr[i] == '{' or arr[i] == '(':
            stack.append(arr[i])
        if stack : 
            if arr[i] == ']':
                if stack[-1] =='[':
                    stack.pop()
            elif arr[i] == ')':
                if stack[-1] =='(':
                    stack.pop()
            elif arr[i] == '}':
                if stack[-1] =='{':
                    stack.pop()
    if len(stack) == 0:
        return True
    return False
    
def solution(s):
    answer = 0
    current_s = deque(s)

    
    for i in range(len(current_s)):
        if check(current_s) :
            answer += 1
        current_s.rotate(-1)
    
    return answer

# --------------------------------------------------------------------