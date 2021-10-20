class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0 
        jewels = list(jewels)
        for cur in stones :
            if cur in jewels :
                ans += 1
        return ans