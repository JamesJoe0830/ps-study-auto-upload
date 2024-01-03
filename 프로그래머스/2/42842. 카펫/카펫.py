# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 42842. 기능개발 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 구현(Implementation)
# ⏰ 걸린 시간 : 21분
# 
# [문제 풀이]
# 0. 완전탐색이지만, 수학적으로 접근해서 이차방정식으로 풀었다.
# brown : 바깥 테두리 블록의 개수
# yellow : 안쪽 블록의 개수
# 1. brown에서 모서리 4개 빼고 나머지 개수가 안쪽 블록을 감싸고 있는 블록이다.
# 2. 이 말은 가로 세로를 곱하면 안쪽 테두리의 개수가 나온다는 말이다.
# 3. 이를 통해서 (brown - 4) / 2 의 값으로 가로세로를 구하고 곱하면 yellow가 나오기 때문에
# 4. 이차방정식의 접근이 가능해진다.
# --------------------------------------------------------------------------------
import math
def solution(brown, yellow):
    answer = []
    except_angle = brown - 4 
    except_angle_divide = except_angle // 2
    # x = except_angle_divide - y
    # x*y = yellow

    width = ((except_angle_divide + math.sqrt(except_angle_divide**2 - 4*yellow))//2) + 2
    height = ((except_angle_divide - math.sqrt(except_angle_divide**2 - 4*yellow))//2) + 2

    answer.append(width)
    answer.append(height)
    
    
    return answer
# --------------------------------------------------------------------------------