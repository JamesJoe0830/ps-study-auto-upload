# 순열과 조합을 접근할 때 backtraking 으로 접근해야 깔끔하다.
import itertools
import math
def check(number): # 소수를 구해주는 애
    for i in range(2, int(number**(1/2))+1):
        if number % i ==0:
            return False
    return True
def solution(numbers):
    answer = 0
    numlist = []
    permutation = set()
    for num in numbers: 
        numlist.append(num)
    for i in range(1,len(numlist)+1):
        per = list(itertools.permutations(numlist,i))
        for j in range(len(per)):
            if int(''.join(per[j])) not in permutation and int(''.join(per[j])) > 1:
                permutation.add(int(''.join(per[j])))
                if check(int(''.join(per[j]))):
                    print(int(''.join(per[j])))
                    answer +=1
    return answer