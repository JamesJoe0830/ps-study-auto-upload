def solution(n, wires):
    answer = 10000

    def dfs(n):
        nonlocal cnt
        print("n",n,"cnt",cnt)
        cnt = 1
        
        visited.add(n)
        for next_node in nums[n]:
            if next_node not in visited:
                print("next_node",next_node)
                cnt += dfs(next_node)
        return cnt
    for i in range(len(wires)):
        nums = [[] for _ in range(n+1)]
        visited = set()
        for j in range(len(wires)):
            if i != j :        
                nums[wires[j][0]].append(wires[j][1])
                nums[wires[j][1]].append(wires[j][0])
        # print(nums)
        dfs_call = []
        for k in range(1,n+1):
            
            if k not in visited:
                cnt =1 
                dfs_call.append(dfs(k))

        print(dfs_call)
        if len(dfs_call) == 2:
            answer = min(abs(dfs_call[0]-dfs_call[1]),answer)

    return answer