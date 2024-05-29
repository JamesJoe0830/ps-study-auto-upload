# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 12924. 숫자의 표현 [🥈 LEVEL2]
# 📚 알고리즘 분류: 수학
# ⏰ 걸린 시간 : 8분
# 시간 복잡도 : O(n*m)
# 
# [문제 풀이]
# 0. 1부터 n까지 start값을 정해서 시작한다.
# 1. n까지 계속해서 증가시키는데 이때 total이 n을 초과하지 않도록 증가시킨다.
# 2. total과 일치하는지 비교해서 같다면 1을 더한다.
# --------------------------------------------------------------------

def solution(n):
    answer = 0
    for i in range(1,n+1):
        start = i
        total = start
        while total < n:
            start += 1
            total += start
        if total == n :
            answer += 1
        print(i,total)
    return answer

# --------------------------------------------------------------------
