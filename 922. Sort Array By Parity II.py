class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)) :
            if nums[i] % 2 :
                odd.append(nums[i])
            else :
                even.append(nums[i])
        ans = []
        for i in range(len(nums)) :
            if i % 2 :
                ans.append(odd[0])
                odd.pop(0)
            else :
                ans.append(even[0])
                even.pop(0)
        return ans