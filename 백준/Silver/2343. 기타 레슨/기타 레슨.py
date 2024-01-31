# https://www.acmicpc.net/problem/2343
# 2343. 기타 레슨 [🥈 실버 1]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 23분
# 🔥 이분 탐색인데 범위의 구간을 정하는게 중요하다.(start값을 정하는게 진짜 중요)
# [풀이방법]
# 0. 전형적인 이분 탐색이다.
# 1. start와 end 값으로 해당 조건을 만족하는지 계속해서 탐색하면 된다.
# 2. 조건은 total에 더하기 이전에 time을 더한 값이 mid 보다 크다면
# 3. total을 리셋하고 블루레이 크기에 하나를 더해준다.
# 4. 총 블루레이를 M과 비교하고 그에 따라 이분탐색을 진행하면 된다.
# ----------------------------------------------------------------------

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lectures = list(map(int,input().split()))

# start,end는 블루레이를 담을 수 있는 공간이다.
start = max(lectures) # 🔥 얘를 1로 설정했더니 애먹었다 .. 블루레이 하나를 담기 위해서는 max(lecture)가 최소값이다.
end = sum(lectures)

while start <= end :
    mid = (start + end)//2
    total = 0 #블루레이의 크기
    count = 1 #블루레이 개수
    for time in lectures:
        if total + time > mid:
            count +=1
            total = 0
        total += time

    if count <= M:
        end = mid - 1
    else:
        start = mid + 1
print(end+1)        

# ----------------------------------------------------------------------
