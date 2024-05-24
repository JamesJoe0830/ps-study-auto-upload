def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    arr.sort()
    answer = str(arr[0]) +' ' + str(arr[-1])
    return answer