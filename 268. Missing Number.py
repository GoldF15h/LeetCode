class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        _len = len(nums)
        for i in range(_len) :
            if nums[i] != i :
                return i
        return nums[-1] + 1