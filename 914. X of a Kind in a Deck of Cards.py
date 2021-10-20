def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
        
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1 :
            return False
        d = {}
        for cur in deck :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        l = list(d.values())
        if len(l) == 1 :
            for i in range(2,l[0]+1) :
                if l[0] % i == 0 :
                    return True
            return False
        else :
            ans = l[0]
            for i in range(1,len(l)) :
                ans = gcd(ans,l[i])
            if ans == 1 :
                return False
            return True