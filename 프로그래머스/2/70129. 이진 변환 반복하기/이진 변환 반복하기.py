def solution(s):
    answer = []
    cnt = 0
    remove = 0
    ex = 21
    
    while s != '1' :
        c_remove = 0
        for i in range(len(s)) :
            if s[i] == '0':
                c_remove +=1
        c_length = (len(s) - c_remove)
        s = format(c_length,'b')
        remove += c_remove
        cnt += 1
    answer = [cnt, remove]
    return answer
