class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 0
        tmp = sorted(nums)
        if tmp[-1] >= tmp[-2]*2 :
            return nums.index(tmp[-1])
        else :
            return -1