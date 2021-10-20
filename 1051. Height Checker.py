class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sHeights = sorted(heights)
        ans = 0
        for i in range(len(sHeights)) :
            if sHeights[i] != heights[i] :
                ans += 1 
        return ans