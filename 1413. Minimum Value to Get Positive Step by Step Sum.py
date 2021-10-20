class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = 1
        _sum = 0
        for cur in nums :
            _sum += cur 
            if _sum < 1 :
                if _sum < _min :
                    _min = _sum
        if _min == 1:
            return _min
        return abs(_min)+1