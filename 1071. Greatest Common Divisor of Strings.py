def isDivisible (s,sub) :
    subIndex = 0
    if len(s) % len(sub) != 0 :
        return False
    for i in range(len(s)) :
        if s[i] == sub[subIndex] :
            subIndex = (subIndex + 1)%len(sub)
        else :
            return False
    return True

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2) :
            str1,str2 = str2,str1

        for i in range( len(str2) , 0 , -1 ) :
            pattern = str2[:i:]
            if isDivisible(str1,pattern) and isDivisible(str2,pattern) :
                return pattern
        return ''


