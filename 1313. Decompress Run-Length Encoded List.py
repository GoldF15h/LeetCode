class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        val = nums[1::2]
        freq = nums[0::2]
        ans = []
        for i in range(len(val)) :
            ans += [val[i]]*freq[i]
        return ans