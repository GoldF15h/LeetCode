class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        _sum = sum(nums)
        nums.sort()
        nums = nums[::-1]
        
        tmp = 0
        for i in range(len(nums)) :
            tmp += nums[i]
            if tmp > _sum - tmp :
                return nums[:i+1:]
        