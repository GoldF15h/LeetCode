class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        _len = len(nums)
        i = 0
        while i < _len :
            if nums[i] == 0 :
                nums.pop(i)
                _len -= 1
                count += 1
                if _len == 0 :
                    break
            else :
                i += 1
        for i in range(count) :
            nums.append(0)