class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        self.k = k

    def add(self, val: int) -> int:
        self.l.append(val)
        self.l.sort()
        return self.l[-1*self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)