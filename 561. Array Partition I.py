class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        op = 0
        for i in range(len(nums)-2,0-1,-2) :
            op += nums[i]
        return op