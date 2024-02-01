# https://www.acmicpc.net/problem/9935
# 9935. 문자열 폭발 [🥇 골드4] 🔥 오답 필요
# 📚 알고리즘 분류: 스택 [STACK]
# ⏰ 걸린 시간 : 23분
# 
# [문제 풀이]
# 0. stack에 집어 넣는다. 
# 1. stack에 넣을때 마지막 값이 boom의 마지막값과 일치하다면
# 2. 여태 넣은 값의 뒤에 값을 boom하고 비교하고 정확하게 일치하다면
# 3. stack 에서 boom길이 만큼 빼준다.
# ---------------------------------------------------------------- 

import sys
input = sys.stdin.readline

word = input().rstrip()
boom = input().rstrip()
stack = []
for i in word:
    stack.append(i)

    if stack[-1] == boom[-1]:
        if "".join(stack[len(stack)-len(boom):]) == boom:
            for i in range(len(boom)):
                stack.pop()
        
# 출력
if stack :
    print("".join(stack))
else:
    print("FRULA")

# ---------------------------------------------------------------- 
