class Solution:
    def longestPalindrome(self, s: str) -> str:
        _len = len(s) 
        for checkRange in range(_len,0,-1) :
            for start in range(0,_len-checkRange+1) :
                curSubArr = s[start:start+checkRange]
                if curSubArr == curSubArr[::-1] :
                    return curSubArr
        return 0