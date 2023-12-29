def solution(array, commands):
    answer = []
    for j in range(len(commands)):
        arr= commands[j]
        li = []
        for i in range(arr[0]-1,arr[1]):
            li.append(array[i])
            li.sort()
        answer.append(li[arr[2]-1])
    return answer


    
