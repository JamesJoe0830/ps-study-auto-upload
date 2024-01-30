# https://www.acmicpc.net/problem/6236
# 6236. 용돈 관리 [🥈 실버 2]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 32분
# 🔥 이분 탐색인데 범위의 구간을 정하는게 중요하다.(start값을 정하는게 진짜 중요)
# [풀이방법]
# 0. 전형적인 이분 탐색이다.
# 1. start와 end 값으로 해당 조건을 만족하는지 계속해서 탐색하면 된다.
# 2. for문은 다음과 같다.
# 2-1. 갖고있는 돈보다 만일 적다면 한번 인출하고 인출한 금액에서 당일 사용을 뺀다.
# 2-2. 이때 갖고있는 돈을 모두 집어 넣고 인출 금액으로 시작한다. -> ❗️start값 결정 요인 
# 2-3. 만일 갖고 있는 돈이 크다면 인출하지 않고 빼주면된다.
# ----------------------------------------------------------------------

import sys
input = sys.stdin.readline
# 만약 K원이 필요한데 없으면 다 집어넣고 K원을 다시 뽑는다.

N, M = map(int,input().split())
#  i번째에 이용할 돈
spend_list = list(int(input()) for _ in range(N))

# start, end 값 세팅
start = max(spend_list) # spend_list중에서 가장 큰 값(다시 돈을 넣고 뽑았을때 충당할 수 있어야한다.)
end = sum(spend_list)


while start <= end :
    withdraw = (start + end)//2
    withdraw_cnt = 1
    have = withdraw # 인출하고 남은돈(갖고 있는 돈)
    for spend in spend_list:
        if have >= spend :
            have -= spend
        else:
            withdraw_cnt += 1
            have = withdraw
            have -= spend
    if withdraw_cnt <= M: #뽑아야하는 횟수보다 뽑은 회수가 적다. => 돈을 많이 뽑았다.
        end = withdraw - 1
    else:
        start = withdraw + 1
print(withdraw)

# ----------------------------------------------------------------------
