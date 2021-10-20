class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        ans = []
        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= _max)
        return ans