def solution(arr):
    answer = []
    result=0
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer