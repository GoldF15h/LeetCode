class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score)[::-1]
        d = {}
        for i in range(len(rank)) :
            med = -1
            if i == 0 :
                med = 'Gold Medal'
            elif i == 1 :
                med = "Silver Medal"
            elif i == 2 :
                med = "Bronze Medal"
            else :
                med = str(i+1)
            d.update({rank[i]:med})
        ans = []
        for i in score :
            ans.append(d[i])
        return ans