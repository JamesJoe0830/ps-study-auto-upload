# https://www.acmicpc.net/problem/2512
# 2512. 예산 [🥈 실버 2]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 7분
# 
# [풀이방법]
# 0. 전형적인 이분 탐색이다.
# 1. start와 end 값으로 해당 조건을 만족하는지 계속해서 탐색하면 된다.
# 2. 조건은 asset이 만일 mid 값보다 작다면 total에 asset을 더해주고 
# 3. asset이 mid 값보다 크다면 total에 mid를 더해준다.
# 4. 총 예산을 M과 비교하고 그에 따라 이분탐색을 진행하면 된다.
# ----------------------------------------------------------------------

import sys
input = sys.stdin.readline
N = int(input()) # 총 지방수
request_assets = list(map(int,input().split()))
M = int(input()) # 총예산
start = 1

end = max(request_assets)

while start<=end :
    mid = (start + end) // 2
    total = 0
    for asset in request_assets:
        if asset <= mid :
            total += asset
        else: 
            total += mid
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# ----------------------------------------------------------------------