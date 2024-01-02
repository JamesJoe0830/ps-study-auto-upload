def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        visited = set()
        def diff(word1,word2):
            different = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    different +=1
            return different
    
        def dfs(word,layer):
            nonlocal answer
            print("AA",visited)
            print(answer, word)
            if word == target :
                return answer

            for j in range(len(words)):
                if j not in visited and diff(word, words[j]) == 1:
                        visited.add(j)
                        next_word = words[j]
                        for i in range(len(next_word)):
                            if next_word[i] != target[i]:
                                dfs(next_word,layer+1)
                                break

        dfs(begin,0)
    return answer