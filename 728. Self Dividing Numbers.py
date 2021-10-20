def isSelfDividing (n) :
    tmp = n 
    while tmp > 0 :
        if tmp % 10 == 0 :
            return False
        if n % (tmp%10) != 0 :
            return False
        tmp //= 10
    return True
            

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1,1) :
            if isSelfDividing(i) :
                ans.append(i)
        return ans