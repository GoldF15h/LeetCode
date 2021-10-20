class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int,date.split('-'))
        ans = 0
        if y % 4 == 0 :
            mArr = [31,29,31,30,31,30,31,31,30,31,30,31]
        else :
            mArr = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(m-1) :
            ans += mArr[i]
        ans += d
        return ans