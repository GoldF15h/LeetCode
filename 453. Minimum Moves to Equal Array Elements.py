class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = min(nums)
        op = 0
        for cur in nums :
            op += cur - _min
        return op