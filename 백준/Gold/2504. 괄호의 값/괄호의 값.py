# https://www.acmicpc.net/problem/2504
# 2504. 괄호의 값 [🥇 골드5] 🔥 오답 필요
# 📚 알고리즘 분류: 스택 [STACK]
# ⏰ 걸린 시간 : 50분
# 
# [문제 풀이]
# 0. stack은 올바른 배열인지를 검사해주는 역할이다.
# 1. ( 나 [ 의 값을 만나면 stack에 넣어주고 각각 ( 는 tmp= 1(임의의 값)에 곱하기 2 [ 는 곱하기 3을 한다.
# 2. ) 나 ] 를 만났다면 여기서 케이스를 분류한다.
# 2-0. 먼저 )라면 tmp // 2 를 하고 ] 라면 tmp // 3을 한다.
# 2-1. ) 일 경우 직전의 값이 ( 인지를 확인하고 맞다면 answer에 tmp를 더한다.
# 2-1. ] 일 경우 직전의 값이 [ 인지를 확인하고 맞다면 answer에 tmp를 더한다.
# 2-2. 만일 직전값이 ( 가 아니라면 answer에 더하지 않는다.
# 2-2. 만일 직전값이 [ 가 아니라면 answer에 더하지 않는다.
# 3. 마지막은 모든 순회를 마치고 stack 이 남아있는지 여부에 따라서 정답을 추출한다.
# ---------------------------------------------------------------- 
import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []

tmp = 1
answer = 0
for i in range(len(arr)):
    if arr[i] == "(" :
        stack.append(arr[i])
        tmp *= 2
    elif arr[i] == "[" :
        stack.append(arr[i])
        tmp *= 3 
    elif arr[i] == ")" :
        if len(stack) == 0 or stack[-1] !="(":
            answer = 0
            break
        if arr[i-1] == "(":
            answer += tmp
        tmp //= 2
        stack.pop()
    elif arr[i] == "]" :
        if len(stack) == 0 or stack[-1] != "[":
            answer = 0
            break
        if arr[i-1] == "[":
            answer += tmp
        tmp //= 3
        stack.pop()
        
if stack :
    print(0)
else :
    print(answer)