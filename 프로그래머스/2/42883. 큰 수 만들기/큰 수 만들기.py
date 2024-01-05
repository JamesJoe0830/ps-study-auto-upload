# import itertools
# nums = list(number)
    # coll = list(map(lambda x : "".join(x),itertools.combinations(nums,len(number)-k)))
    # answer=str(max(coll))
    

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k>0:
            k-=1
            stack.pop()
        stack.append(num)
    if k != 0 :
        stack = stack[:-k]
    answer = "".join(stack)
        
    return answer