class Solution:
    def reverseString(self, s: List[str]) -> None:
        _len = len(s)
        for i in range(_len//2) :
            s[i],s[_len-1-i] = s[_len-1-i],s[i]