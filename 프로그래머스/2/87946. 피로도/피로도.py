# backtracking으로 해결해보자 permutaition 시간복잡도 O(n!)이므로
import itertools
def solution(k, dungeons):
    answer = 0

    permu = list(itertools.permutations(dungeons,len(dungeons)))
    # print(permu)
    for dungeons in permu:
        cnt = 0
        fatigue = k
        # print(dungeons)
        for need_min, use_fatigue in dungeons:
            if fatigue >= need_min and fatigue >=use_fatigue:
                fatigue -= use_fatigue
                cnt +=1
        answer = max(cnt, answer)

    return answer