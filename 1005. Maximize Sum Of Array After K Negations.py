class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        i = 0
        while i < len(nums) :
            if nums[i] > 0 :
                break
            elif k > 0 :
                nums[i] = nums[i] * -1
                k -= 1
            else :
                break
            i+= 1
            
        if k % 2 == 1 :
            minIndex = 0
            for i in range(len(nums)) :
                if nums[i] < nums[minIndex] :
                    minIndex = i
            nums[minIndex] = nums[minIndex]*-1
        
        return sum(nums)