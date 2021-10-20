class Solution:
    def maxScore(self, s: str) -> int:
        zeroCnt = 0
        oneCnt = 0
        ans = 0
        
        for cur in s :
            if cur == '1' :
                oneCnt += 1
                
        for i in range(len(s)-1) :
            if s[i] == '1' :
                oneCnt -= 1
            if s[i] == '0' :
                zeroCnt += 1
            if oneCnt + zeroCnt > ans :
                ans = oneCnt + zeroCnt
                
        return ans
        