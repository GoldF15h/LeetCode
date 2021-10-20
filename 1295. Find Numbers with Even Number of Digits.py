class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for cur in nums :
            digit = 0
            while 10**digit <= cur :
                digit += 1
            # print(digit)
            if digit % 2 == 0 :
                ans += 1
        return ans