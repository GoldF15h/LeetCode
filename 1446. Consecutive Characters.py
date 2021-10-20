class Solution:
    def maxPower(self, s: str) -> int:
        curChr = s[0]
        ans = 0
        curCnt = 1
        for i in range(1,len(s)) :
            # print(curChr,i,ans)
            if s[i] == curChr :
                curCnt += 1
            else :
                if ans < curCnt :
                    ans = curCnt
                curChr = s[i]
                curCnt = 1
        if ans < curCnt :
            ans = curCnt
        return ans
            