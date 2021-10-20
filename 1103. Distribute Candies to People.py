class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = []
        for i in range(num_people) :
            ans.append(0)
        cur = 1
        i = 0
        while candies > 0 :
            if cur >= candies :
                ans[i] += candies
                return ans
            else :
                ans[i] += cur
                candies -= cur
                cur += 1
                i = (i+1)%num_people