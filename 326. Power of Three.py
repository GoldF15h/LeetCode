class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        count = 0
        
        if n == 1:
            return True
        
        if n < 3 :
            return False
        
        while n > 1 :
            if n % 3 != 0 :
                return False
            n /= 3
            count += 1
        return True