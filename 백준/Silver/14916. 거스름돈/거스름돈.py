# https://www.acmicpc.net/problem/14916
# 14916. 거스름돈 [🥈 실버5]
# 📚 알고리즘 분류: 그리디(Greedy)
# ⏰ 걸린 시간 : 10분
# 
# [문제 풀이]
# 0. 2차 방정식을 세우고 5x + 2y = 15
# 1. 5의 최대로 가질 수 있는 값고 2의 최소 몫을 구하고
# 2. 2차 방정식을 만족하지 않다면 x의 값을 1씩 낮추고 그때의 y의 값을 구하면 된다.
# ---------------------------------------------------------------- 
import sys
input = sys.stdin.readline
N = int(input())
answer = 0
# x개 y개 
# 5x + 2y = 15
x = N//5
y = (N%5)//2
while True:
    if 5*x + 2*y == N :
        print(x+y)
        break
    elif x == 0 :
        if 5*x + 2*y !=N:
            print(-1)
            break
    else:
        x -=1
        y = (N-5*x) //2