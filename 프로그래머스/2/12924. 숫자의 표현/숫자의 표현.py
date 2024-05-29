def solution(n):
    answer = 0
    for i in range(1,n+1):
        start = i
        total = start
        while total < n:
            start += 1
            total += start
        if total == n :
            answer += 1
        print(i,total)
    return answer