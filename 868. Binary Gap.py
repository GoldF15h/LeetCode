class Solution:
    def binaryGap(self, n: int) -> int:
        bi = []
        while n > 0 :
            bi.append(n%2)
            n//=2
            
        oneIndex = []
        for i in range(len(bi)) :
            if bi[i] == 1 :
                oneIndex.append(i)
                
        ans = 0
        for i in range(len(oneIndex)-1) :
            cur = oneIndex[i+1] - oneIndex[i]
            if cur > ans :
                ans = cur
                
        return ans