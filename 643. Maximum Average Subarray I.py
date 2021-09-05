class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k:])
        ans = cur
        l = nums[:k:]
        for i in range(k,len(nums)) :
            cur += nums[i] - l[0]
            l.append(nums[i])
            l.pop(0)
            if ans < cur :
                ans = cur
        return ans/k
        