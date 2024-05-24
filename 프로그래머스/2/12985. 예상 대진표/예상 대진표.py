#       1                  2
#    1       2        3.         4
#  1   2   3   4   5.    6.    7     8
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
def solution(n,a,b):
    answer = 0

    while a!=b :
        a= (a+1) // 2
        b= (b+1) // 2
        answer += 1
            
    return answer