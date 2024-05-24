# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 12981. 영어 끝말잇기 [🥈 LEVEL2]
# 📚 알고리즘 분류: 구현
# ⏰ 걸린 시간 : 25분
# 시간 복잡도 : O(n*m) m:visited 개수
# 
# [문제 풀이]
# 0. 앞 단어에 끝문자와 뒤 단어의 앞문자를 비교해서 같지 않다면, 탈락자 발생
# 1. visited 배열을 순회하면서 이미 나온 단어라면 탈락자 발생
# if) 탈락자 발생 -> check함수로 [번호, 차례]를 계산
# --------------------------------------------------------------------

import math
# [번호, 차례]를 체크해주는 함수
def check(i,n,answer):
    person = i % n
    if person == 0:
        person = n
    order = math.ceil(i / n)
    answer = [person, order]
    return answer
        

def solution(n, words):
    answer = [0,0] # [번호, 차례]
    visited = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in visited:
            if visited[-1][-1] == words[i][0]:
                visited.append(words[i])
            else:
                answer = check(i+1, n,answer)
                break
        else:
            answer = check(i+1, n,answer)
            break
        
        
    return answer
