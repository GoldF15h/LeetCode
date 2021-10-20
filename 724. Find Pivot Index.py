class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        prev = 0
        for i in range(len(nums)) :
            left_sum += prev
            prev = nums[i]
            right_sum -= nums[i]
            if left_sum == right_sum :
                return i
        return -1