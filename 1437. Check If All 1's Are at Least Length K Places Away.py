class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curDis = 0
        i = 0
        while i < len(nums) and nums[i] != 1 :
            i += 1
        i += 1
        while i < len(nums) :
            if nums[i] == 1 :
                if curDis >= k :
                    curDis = 0
                else :
                    return False
            else :
                curDis += 1
            i += 1
        return True