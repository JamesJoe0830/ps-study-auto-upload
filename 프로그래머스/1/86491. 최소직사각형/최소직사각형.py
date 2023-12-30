def solution(sizes):
    answer = 0
    a=0
    j,k =0, 0
    for i in range(len(sizes)):
        if(sizes[i][0]<sizes[i][1]):
            a=sizes[i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=a
        j = max(sizes[i][0], j)
        k = max(sizes[i][1], k)
        
    
    return j*k