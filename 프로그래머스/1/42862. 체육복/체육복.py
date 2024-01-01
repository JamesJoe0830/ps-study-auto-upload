# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 42862. 체육복 [🥈 LEVEL 1]
# 📚 알고리즘 분류: Greedy(탐욕법)
# ⏰ 걸린 시간 : 40분
# 시간 복잡도 : O(n^2)
# 
# [풀이 방법]
# 0. 빌려준 친구들을 제거하는 배열을 만든다.
# 1. 빌려주는 애가 이미 빌려주거나 도난 안당했을 경우에 빌려주도록 하고 빌려준 명단에 추가한다.
# 2. 빌려주는 기준은 앞뒤로 빌려줄 수 있다.
# [주의 할 점]
# lost와 reserve 를 sort를 하지 않으면 5, [4, 2], [3, 5] 이렇게 될때
# 4는 3에게 빌리고 2는 5에게 못빌리는 상황이 생긴다.
# 이런 상황이 발생한 이유는 앞뒤로 비교하는 로직이 정렬되어 있지 않으면 발생하는 문제이다.
# -------------------------------------------------------------------------------------

def solution(n, lost, reserve):
    answer = 0
    len_lost = 0 #잃어 버린 친구들
    check = [] # 빌려준 친구들은 제외하기 위한 배열
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        if lost[i] not in reserve :
            len_lost += 1
            for j in range(len(reserve)):
                print("check",i,j,check)
                if reserve[j] not in check and reserve[j] not in lost: #빌려주는 애가 이미 빌려주거나 도난 안당했을 경우
                    if lost[i] - 1 == reserve[j]: # 잃어버린 친구의 이전번호가 reserve에 있으면 빌려준 명단에 추가
                        check.append(reserve[j])
                        break
                    elif lost[i] + 1 == reserve[j]: # 잃어버린 친구의 다음번호가 reserve에 있으면 빌려준 명단에 추가
                        check.append(reserve[j])
                        break
    print(len_lost)
    print(check)
    answer = n - len_lost + len(check)
    return answer
# -------------------------------------------------------------------------------------