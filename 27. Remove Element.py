def sol (nums,val) :
    i = 0 
    _len = len(nums)
    while i < _len :
        if nums[i] == val :
            nums.pop(i)
            _len = _len - 1
        else :
            i = i + 1 
    
    return _len
    

if __name__ == "__main__" :
    nums = list(map(int,input().strip('[]').split(',')))
    val = int(input())
    print(sol(nums,val))