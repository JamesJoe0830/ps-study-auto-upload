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

start = 110
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

