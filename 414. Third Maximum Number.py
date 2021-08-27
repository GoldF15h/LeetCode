class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        _len = len(nums)
        if _len >= 3 :
            return nums[-3]
        else :
            return nums[-1]