import sys
input = sys.stdin.readline
X = int(input())
answer = 0

if X <= 99:
    print(X)
elif X > 99:
    answer = 99
    i = 100
    while True:
        if i > X:
            print(answer)
            break
        if i < 1000:
            a=i//100
            b=(i-a*100)//10
            c=(i-a*100-b*10)//1

            if b-a == c-b:
                answer +=1
            i+=1 
        elif i == 1000:
            d=i//1000
            a=(i-d*1000)//100
            b=(i-d*1000-a*100)//10
            c=(i-d*1000-a*100-b*10)//1
            if a-d == b-a and b-a == c-b:
                answer +=1
            i+=1