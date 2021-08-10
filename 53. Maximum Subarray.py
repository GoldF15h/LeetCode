def toQuickSumArr (arr,_len) :
    _sum = 0
    for i in range(_len) :
        _sum = _sum + arr[i]
        arr[i] = _sum
    # print(arr)
    return arr

def findMaxA_B (arr,_len,_max) :
    a = arr[0]
    b = arr[1]
    bIndex = 1
    for i in range(1,_len):
        if b < arr[i] :
            b = arr[i]
            bIndex = i
    for j in range(bIndex-1):
        if a > arr[i] :
            a = arr[i]
    # print(a-b,_max)
    if b-a > _max :
        _max = b-a

    return _max

def sol (nums) :
    _len = len(nums)

    if _len == 1 :
        return nums[0]
    if _len == 0 :
        return 0

    _max = max(nums)

    nums = toQuickSumArr(nums,_len)

    _ = max(nums)
    if _max < _ :
        _max = _

    return findMaxA_B(nums,_len,_max)
    

if __name__ == "__main__" :
    n = list(map(int,input().strip('[]').split(',')))
    # print(n)
    print(sol(n))