# 유클리드 호제법으로 최대공약수 구하고
# 모든 수를 최대공약수로 나누면서 곱하면 된다.
def solution(arr):
    answer = 1
    for i in (arr):
        answer = lcm(answer,i)

    return answer


def gcd(a,b):
    while b:
        a, b = b, a%b
        
    return a

def lcm(a, b) :
    answer = (a*b) // gcd(a, b)
    
    return answer