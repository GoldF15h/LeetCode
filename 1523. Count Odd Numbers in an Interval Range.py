class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high :
            if low % 2 == 1 :
                return 1
            return 0
        
        if low % 2 == 0 :
            low += 1
        if high % 2 == 0 :
            high -= 1
            
        if low == high :
            return 1
        
        return (high - low)//2 + 1
            