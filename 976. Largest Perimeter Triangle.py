class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = []
        ans = 0
        while len(nums) > 0 :
            l.append(nums[-1])
            nums.pop()
            if len(l) == 3 :
                if l[0] < l[1] + l[2] and ans < l[0] + l[1] + l[2] :
                    ans = l[0] + l[1] + l[2]
                l.pop(0)
        return ans