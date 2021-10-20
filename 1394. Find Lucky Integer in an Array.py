class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for cur in arr :
            if d.get(cur) :
                d[cur] += 1 
            else :
                d.update({cur:1})
        ans = -1
        for cur in d.keys() :
            if d[cur] == cur :
                if cur > ans :
                    ans = cur
        return ans
                