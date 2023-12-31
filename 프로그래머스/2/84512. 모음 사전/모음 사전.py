# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 84512. 모음 사전 [🥈 LEVEL2]
# 📚 알고리즘 분류: 수학 🔥 오답 필요 (해당 문제의 사고력 부분)
# ⏰ 걸린 시간 : 50분
# 시간 복잡도 : O(n)
# 
# [풀이 방법]
# 0. 각 자리수 별로 시작하는 수가 다르다. 1자리는 1부터 시작, 2자리는 2부터 시작
# 1. 자리수 별로 증가하는 값도 다르다.
# 2. 진수의 개념으로 접근한다.

# 6진수개념이다.
# A는 결국 0승
# AAAAA => 5
# E는 4번째자리 : 10,
# I는 4번째자리 : 16,
# O는 4번째자리 : 22,
# U는 4번째자리 : 28,
# --------------------------------------------------------------------------------- 
def solution(word):
    answer = 0
    word_index = ["A","E","I","O","U"]
    binary = [781,156,31,6,1]
    # A :"1" AA:"2" AAA:"3" AAAA:"4" AAAAA:"5"
    # 자리수 만큼을 더해준다.
    for i in range(len(word)):
        find_word_index= word_index.index(word[i])
        answer += find_word_index*binary[i]
    # 자리수 별로 시작하는 값도 다르기 때문에 AAA는 3이고 A는 1이다.
    answer += len(word)
    
    return answer
# --------------------------------------------------------------------------------- 
    # A
    # AA
    # AAA
    # AAAAA
    # 1. AAAAE : 1 + 5
    # 2. EIO  :781 + 156 * 2 + 31 * 3 + 3
    #.              312     93.   3
    # 3. AAAE : 6*1 + 4 = 10
    # 4. AAAI : 12 + 4
    # EIOA : 4 + 781 + 156 * 2 + 31*3 + 6

    # AAAAA
    # 6증가
    # AAAAA
    # AAA => 3
    # AAAE. 10
    # AAAEA 11
    # AAAEE 12
    # AAAEI 13
    # AAAEO 14
    # AAAEU 15
    # AAAI  16 -> 6 (5 + 1)
    # AAAU  28
#     AAAUA 29
#     AAAUE 30
#     AAAUI 31
#     AAAUO 32
#     AAAUU 33
#.    AAE   34 [31 -> (6*5 + 1)]


    # 0  1  2  3  4  5
    # 10 11 12 13 14 15
    # 20 21 2 23 24 25
    # 30 31 32 33 34 35
    # 40 41 42 43 44 45
    # 50 51 52 53 54 55
    # 100
    # 6진수로 놓고 자리수 별로 변화하는 값이 다르다.
    # 1씩 변화한다.
    # 2의 자리는 10씩 변화한다.
    # 3의 자리는 100씩 변화한다.