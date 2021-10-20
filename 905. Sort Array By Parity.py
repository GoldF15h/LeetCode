class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenList = []
        oddList = []
        for cur in nums :
            if cur % 2 :
                oddList.append(cur)
            else :
                evenList.append(cur)
        return evenList + oddList