class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        _min = min(nums)
        if _max - _min <= k*2:
            return 0
        return _max - _min - k*2
        