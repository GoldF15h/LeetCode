class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = []
        count = 0
        curStr = ''
        ans = 0
        for i in range(len(s)) :
            # print(s[i],curStr)
            if s[i] != curStr :
                l.append(count)
                count = 1
                curStr = s[i]
            else :
                count += 1
        l.append(count)
        l.pop(0)
        for i in range(len(l)-1) :
            ans += min(l[i],l[i+1])
        return ans
            
        