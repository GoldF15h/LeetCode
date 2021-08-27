class NumArray:

    def __init__(self, nums: List[int]):
        self.l = []
        _sum = 0
        print(nums)
        for i in range(len(nums)) :
            _sum += nums[i]
            self.l.append(_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.l[right]
        return self.l[right] - self.l[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)