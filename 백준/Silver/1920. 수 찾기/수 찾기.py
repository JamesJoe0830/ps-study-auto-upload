# https://www.acmicpc.net/problem/1920
# 1920.수 찾기 [🥈 실버 4]
# 📚 알고리즘 분류: 이진 탐색
# ⏰ 걸린 시간 : 5분
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

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
M = int(input())
find_nums = list(map(int,input().split()))

for find_num in find_nums:
    start = 0
    end = N-1
    find = False
    if nums[-1] < find_num or nums[0] > find_num:
        print(0)
    else:
        while start <= end :
            mid = (start + end)//2
            if nums[mid] == find_num:
                find = True
                break
            elif nums[mid] < find_num:
                start = mid +1 
            elif nums[mid] > find_num:
                end = mid - 1 
        print(int(find))
# ------------------------------------------------------------------
