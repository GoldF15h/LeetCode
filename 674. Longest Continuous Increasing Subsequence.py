def sol (nums) :
    _len = len(nums)
    cur = []
    ans = []
    i = 0
    while i < _len :
        # print(i,cur)
        if len(cur) < 2 :
            if cur == [] or cur[0] < nums[i]:
                cur.append(nums[i])
            else :
                cur = [nums[i]]
            i += 1
        else :
            if nums[i] - cur[-1] > 0 :
                cur.append(nums[i])
                i += 1
            else :
                if len(ans) < len(cur) :
                    ans = cur
                cur = [nums[i-1]]
    if len(ans) < len(cur) :
        ans = cur
    return len(ans)
    

if __name__ == "__main__" :
    n = list(map(int,input().strip('[]').split(',')))
    print(sol(n))