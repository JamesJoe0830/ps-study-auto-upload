# https://www.acmicpc.net/problem/7795
# 7795.먹을 것인가 먹힐 것인가 [🥈 실버 3]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 35분
#
#
# [풀이 방법]
# 0. 이진 탐색을 통해서 O(logN)의 시간복잡도를 갖고 문제를 접근한다.
# 1. Flag를 사용해서 못찾았을 경우 print(0)을 해야한다.
# 2. 이진 탐색을 써서 mid 값을 찾아주고 벗어나면 start end를 재설정 해서 탐색한다.
# 3. start와 end는 새로운 값을 찾을때 초기화해준다.
# ------------------------------------------------------------------

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    answer = 0
    # binary_search(이진 탐색)
    for i in range(N):
        A[i]
        start = 0
        end = M-1
        find_index = -1 #찾고자하는 인덱스가 있는지 검사하기 위한 값
        # 8 1 7 3 1
        # 1 3 6
        while start <= end:
            mid = (start + end)//2

            if A[i] > B[mid]: # 찾고자하는 값이 B인덱스 현재 값보다 크다면 start = mid + 1
                find_index = mid 
                start = mid + 1
            else:
                end = mid - 1
        
        if find_index != -1:
            answer += end+1
    print(answer)

# ------------------------------------------------------------------
# [이분 탐색 라이브러리 사용]---------------------------------------------

# import sys
# from bisect import bisect_left


# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     B.sort()
#     answer = 0
#     for a in A:
#         answer += bisect_left(B,a)

# ------------------------------------------------------------------