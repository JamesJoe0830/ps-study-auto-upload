def solution(answers):
    answer = []
    a =[1, 2, 3, 4, 5]*len(answers)
    b =[2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    c =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    count_a = count_b = count_c = 0
    arr =[]
    
    #  a[i%len(answer)] 이렇게 하면 a,b,c길이 늘리지 않아도 된다.
    for i in range(len(answers)):
        if answers[i] == a[i]:
            count_a += 1
        if answers[i] == b[i]:
            count_b += 1
        if answers[i] == c[i]:
            count_c += 1
    arr = [count_a,count_b,count_c]
    cnt = max(count_a, count_b, count_c)
    for j in range(len(arr)) :
        if cnt == arr[j] :
            answer.append(j+1)
    return answer