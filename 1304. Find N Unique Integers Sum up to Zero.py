class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0 :
            ans = []
        else :
            ans = [0]
        ans = ans + list(range(1,n//2+1)) + list(range(-1,-1*(n//2+1),-1))
        return ans