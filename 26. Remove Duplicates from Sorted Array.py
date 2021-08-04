def sol (nums) :
    i = 0 
    _len = len(nums)

    while i < _len - 1 :
        if nums[i] == nums[i+1] :
            nums.pop(i+1)
            _len = _len - 1 
        else :
            i = i + 1

    return len(nums)

# def sol(nums) :
#     op = [-101]
#     tail = 0
#     for i in nums :
#         if i > tail :
#             op.append(i)
#             tail = tail + 1

#     return tail

if __name__ == "__main__" :
    nums = list(map(int,input().strip('[]').split(',')))
    print(sol(nums))