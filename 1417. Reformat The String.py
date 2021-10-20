class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1 :
            return s
        dig = []
        alp = []
        for cur in s :
            if cur.isnumeric() :
                dig.append(cur)
            elif cur.isalpha() :
                alp.append(cur)
        if dig == [] or alp == [] :
            return ''
        if abs ( len(dig) - len(alp) ) > 1 : 
            return ''
        ans = ''
        if len(dig) < len(alp) :
            dig,alp = alp,dig
        while True :
            if len(dig) > 0 :
                ans += dig[0]
                dig.pop(0)
            if len(alp) > 0 :
                ans += alp[0]
                alp.pop(0)
            if len(dig) == 0 and len(alp) == 0 :
                return ans