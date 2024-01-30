import sys
input = sys.stdin.readline

# 만약 K원이 필요한데 없으면 다 집어넣고 K원을 다시 뽑는다.

N, M = map(int,input().split())
#  i번째에 이용할 돈
spend_list = list(int(input()) for _ in range(N))

start = max(spend_list) # spend_list중에서 가장 큰 값(다시 돈을 넣고 뽑았을때 충당할 수 있어야한다.)
end = sum(spend_list)


while start <= end :
    withdraw = (start + end)//2
    cnt = 1
    have = withdraw # 인출하고 남은돈(갖고 있는 돈)
    for spend in spend_list:
        if have >= spend :
            have -= spend
        else:
            cnt += 1
            have = withdraw
            have -= spend
    if cnt <= M: #뽑아야하는 횟수보다 뽑은 회수가 적다. => 돈을 많이 뽑았다.
        end = withdraw - 1
    else:
        start = withdraw + 1
print(withdraw)