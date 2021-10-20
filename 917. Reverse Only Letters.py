class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        exStr = []
        s = list(s)
        for i in range(len(s)) :
            if s[i].isalpha() :
                exStr.append(s[i])
                s[i] = chr(32)
        for i in range(len(s)) :
            if s[i] == chr(32) :
                s[i] = exStr[-1]
                exStr.pop()
        return ''.join(s)