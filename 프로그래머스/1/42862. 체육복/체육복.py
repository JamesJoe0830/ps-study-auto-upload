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
                    if lost[i] - 1 == reserve[j]: 
                        check.append(reserve[j])
                        break
                    elif lost[i] + 1 == reserve[j]:
                        check.append(reserve[j])
                        break
    print(len_lost)
    print(check)
    answer = n - len_lost + len(check)
    return answer