# https://www.acmicpc.net/problem/1065
# 1065. 한수 [🥈 실버4]
# 📚 알고리즘 분류: 브루트 포스 [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 12분
# 
# [문제 풀이]
# 0. 100 이하는 모두 등차수열이다.
# 1. 그 이후 100 이상 1000 미만은 0번째 1 번째 차이와 1번째 2번째 차이를 같다면 
# 
# ----------------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
hansu = 0
for num in range(1,N+1):
    if num < 100:
        hansu += 1
        # 100 이하는 모두 등차수열
    else:
        if int(str(num)[0])-int(str(num)[1]) ==int(str(num)[1])-int(str(num)[2]):
            hansu += 1
print(hansu)

# ----------------------------------------------------------------
# import sys
# input = sys.stdin.readline
# X = int(input())
# answer = 0

# if X <= 99:
#     print(X)
# elif X > 99:
#     answer = 99
#     i = 100
#     while True:
#         if i > X:
#             print(answer)
#             break
#         if i < 1000:
#             a=i//100
#             b=(i-a*100)//10
#             c=(i-a*100-b*10)//1

#             if b-a == c-b:
#                 answer +=1
#             i+=1 
#         elif i == 1000:
#             d=i//1000
#             a=(i-d*1000)//100
#             b=(i-d*1000-a*100)//10
#             c=(i-d*1000-a*100-b*10)//1
#             if a-d == b-a and b-a == c-b:
#                 answer +=1
#             i+=1
