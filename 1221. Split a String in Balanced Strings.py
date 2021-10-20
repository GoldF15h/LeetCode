class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCnt = 0
        rCnt = 0
        ans = 0
        for i in range(len(s)) :
            if s[i] == 'L' :
                lCnt += 1
            if s[i] == 'R' :
                rCnt += 1
            if lCnt == rCnt :
                ans += 1
                lCnt = 0
                rCnt = 0
        return ans