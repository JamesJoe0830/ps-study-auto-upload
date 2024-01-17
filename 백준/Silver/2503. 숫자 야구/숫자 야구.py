# https://www.acmicpc.net/problem/2503
# 1057. 숫자야구 [🥈 실버3]
# 📚 알고리즘 분류: 브루트 포스 [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 50분
# 
# [문제 풀이]
# 0. start를 111부터 시작하고 증가시킨다. 
# 1. 이때 start 숫자야구로 부른 수들과 각각 비교한다.
# 2. strike와 ball이 부른수들과 모두 일치하면 그때 정답을 1증가
# 3. start값이 strike와 ball이 하나라도 틀리면 바로 다음 수로 넘어간다.
# 
# [실수한 부분]
# 0. 세자리 수는 서로다른 수들로 이뤄져있다. ->이거 못보고 풀어서 계속 오답나옴...
# 1. 수를 증가시키더라도 어느자리라도 0은 포함되면 안된다.
# 
# [브루트 포스]
# 0. N의 개수가 몇 안된다. 브루트 포스로 접근해도 무방하다. 다른 풀이를 사고하다 시간이 오래걸림..
# -------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
num_baseball = []
answer = 0
for i in range(N):
    num, strike, ball = map(int,input().split())
    num_baseball.append((num, strike, ball))

def check(num):
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
            return False
    return True

start = 111
while start < 1000:
    flag = True 
    if "0" not in str(start) and check(str(start)):
        for t in range(N):
            now_num = num_baseball[t][0]
            strike = num_baseball[t][1]
            ball = num_baseball[t][2]
            strike_cnt = 0
            ball_cnt =0
            for i in range(3):
                if str(start)[i] == str(now_num)[i]:
                    strike_cnt +=1
                elif str(start)[i] in str(now_num):
                    ball_cnt += 1
            if strike != strike_cnt or ball != ball_cnt:
                flag = False
                break
        if flag == True:
            answer +=1
    start +=1
    

print(answer)

# -------------------------------------------------------------------------
