# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# 12980. 점프와 순간 이동 [🥈 LEVEL2]
# 📚 알고리즘 분류: stack [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 5분
# 
# [문제 풀이]
# 0. 반복적으로 N을 2를 나눌지 -1을 할지 결정한다.
# 1. 이유는 2로 나누면 건전지 사용량이 안들고 -1을 하면 건전지 사용량(ans)가 1 증가한다.
# 2. n이 0이 된 순간 건전지가 0일때 ans를 출력한다.
# ----------------------------------------------------------------

def solution(n):
    ans = 0
    while True:
        if n == 0:
            break
        if n%2 != 0 :
            n -= 1
            ans += 1
        else:
            n = n // 2

    return ans

# ----------------------------------------------------------------