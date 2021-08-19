def sol(nums) :
    _len = len(nums)
    nums.sort()
    return nums[_len//2]

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    print(sol(l))