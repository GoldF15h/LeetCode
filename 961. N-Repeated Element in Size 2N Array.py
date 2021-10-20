class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)//2
        for cur in nums :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        for cur in d.keys() :
            if d[cur] == n :
                return cur