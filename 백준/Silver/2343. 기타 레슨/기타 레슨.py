import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lectures = list(map(int,input().split()))

start = max(lectures)
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
