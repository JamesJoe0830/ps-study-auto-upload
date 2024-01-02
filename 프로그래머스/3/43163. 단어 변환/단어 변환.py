# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 43163. 단어 변환 [🥈 LEVEL 2]
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 53분
# 
# [풀이 방법]
# 0. recursion DFS로 접근한다. 
# 1. diff를 통해 이전의 단어와 바꾸고자 하는 단어의 값을 비교한다. (하나의 한 단어 만 비교해주기 위해)
# 2. dfs를 돌때 이전의 cnt(바꾼 횟수 값)과 visited 집합을 갖고 계속해서 돈다.
# 3. 각각 dfs를 돌기 떄문에 visited를 갖고 돌아야한다. 
# ---------------------------------------------------------------------
def diff(prev_word,next_word):
        different = 0
        for i in range(len(prev_word)):
            if prev_word[i] != next_word[i]:
                different +=1
        return different

def solution(begin, target, words):
    answer = 0
    def dfs(word, cnt, visited):
        nonlocal answer
        if word == target :
            answer = cnt
            print("answer", answer)
            return answer

        for j in range(len(words)):
            if j not in visited and diff(word, words[j]) == 1 :
                    visited.add(j)
                    dfs(words[j], cnt+1, visited)
                    visited.remove(j) #visited를 각각 bfs마다 다르게 하기 위함이다.

    if target not in words:
        return 0
    else:
        visited = set()
        dfs(begin,0,visited)

        
    return answer
