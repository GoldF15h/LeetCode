class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(len(nums)-1) :
            if nums[i] == nums[i+1] :
                dup_num = nums[i]
                nums.pop(i)
                break
        
        lost_num = len(nums)+1
        for i in range(len(nums)) :
            if nums[i] != i+1 :
                lost_num = i+1
                break

        return [dup_num,lost_num]