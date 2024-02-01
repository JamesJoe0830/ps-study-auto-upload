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
        

if stack :
    print("".join(stack))
else:
    print("FRULA")