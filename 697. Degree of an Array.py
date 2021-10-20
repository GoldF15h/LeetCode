class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for cur in nums :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        _max = max(d.values())
        toFind = []
        for cur in d.keys():
            if d[cur] == _max :
                toFind.append(cur)
        # print(toFind)
        ans = 2**31
        _len = len(nums)
        for cur in toFind :
            head = 0 
            tail = _len - 1
            while nums[head] != cur :
                head += 1
            while nums[tail] != cur :
                tail -= 1
            if tail - head < ans :
                ans = tail-head
        return ans + 1
        