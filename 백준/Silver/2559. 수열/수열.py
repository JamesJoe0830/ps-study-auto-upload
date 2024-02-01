import sys
input = sys.stdin.readline
N, K = map(int,input().split())

temp = list(map(int,input().split()))
pre_sum = sum(temp[0:K])
ans = sum(temp[0:K])
for i in range(1,N-K+1):
    pre_sum += - temp[i-1] + temp[i-1+K]
    if ans < pre_sum:
        ans = pre_sum
print(ans)
    