class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        dec = 0
        ans = []
        for i in range(len(nums)) :
            dec = dec*2 + nums[i]
            # print(dec,dec % 5 == 0)
            if dec % 5 == 0 :
                ans.append(True)
            else :
                ans.append(False)
        return ans