def biSearch (l,t,head,tail) :

    if tail >= head :
        mid = (head + tail) // 2

        if l[mid] == t :
            return mid
        elif l[mid] < t :
            return biSearch(l,t,mid+1,tail)
        else :
            return biSearch(l,t,head,mid-1)

    else :
        return -1

def sol (nums,target) :
    _len = len(nums)
    _max = nums[_len-1]
    _min = nums[0]
    # check in nums == []
    if _len == 0 :
        return 0

    # check if in range
    if nums[0] >= target :
        return 0
    if nums[_len-1] < target :
        return _len

    # if in range
    targetIndex = biSearch(nums,target,0,_len-1)
    while targetIndex == -1 :
        target = target + 1
        targetIndex = biSearch(nums,target,0,_len-1)

    i = targetIndex 
    while nums[i] == target :
        i = i - 1 

    return i + 1

if __name__ == "__main__" :
    n = list(map(int,input().strip('[]').split(',')))
    t = int(input())
    print(sol(n,t))