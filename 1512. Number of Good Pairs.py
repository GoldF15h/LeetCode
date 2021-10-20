class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        
        d = {}
        for cur in nums :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
                
        for cur in d.keys() :
            # print(cur,d[cur]) 
            n = d[cur] - 1
            if n >= 1 :
                ans += (n*(n+1))//2
            
        return ans
        