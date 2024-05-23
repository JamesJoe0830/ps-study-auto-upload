# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 138476. 귤 고르기 [🥈 LEVEL2]
# 📚 알고리즘 분류: 스택
# ⏰ 걸린 시간 : 28분
# 시간 복잡도 : O(nlogn)
# 
# --------------------------------------------------------------------
# 
def solution(k, tangerine):
    answer = 0
    total_len = len(tangerine)
    max_num = max(tangerine)
    box = [0] * (max_num+1)
    size_type = 0 
    for i in range(total_len):
        if box[tangerine[i]] == 0 :
            size_type+=1
        box[tangerine[i]] += 1
    box.sort(reverse=True)
    total_cnt = sum(box) #총 귤의 개수
    answer = size_type 

    while box :
        tangerine_cnt = box.pop()
        if tangerine_cnt != 0:
        
            if total_cnt > k :
                answer -= 1
                total_cnt -= tangerine_cnt
            if total_cnt <= k :
                if total_cnt == k:
                    break
                else:
                    answer +=1
                    break
        
    return answer

# --------------------------------------------------------------------