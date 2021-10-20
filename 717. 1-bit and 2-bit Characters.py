class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        _len = len(bits)
        i = 0
        ans = False
        while i < _len :
            if bits[i] == 0 :
                ans = True
                i += 1
            else :
                ans = False
                i += 2
        return ans
            
            