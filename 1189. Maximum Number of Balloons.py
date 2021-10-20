class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for cur in text :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        ans = 2**32
        
        curChr = 'b'
        if d.get(curChr) :
            if ans > d[curChr] :
                ans = d[curChr]
        else :
            return 0
        
        curChr = 'a'
        if d.get(curChr) :
            if ans > d[curChr] :
                ans = d[curChr]
        else :
            return 0
        
        curChr = 'n'
        if d.get(curChr) :
            if ans > d[curChr] :
                ans = d[curChr]
        else :
            return 0
        
        curChr = 'l'
        if d.get(curChr) :
            if ans > d[curChr]//2 :
                ans = d[curChr]//2
        else :
            return 0
        
        curChr = 'o'
        if d.get(curChr) :
            if ans > d[curChr]//2 :
                ans = d[curChr]//2
        else :
            return 0
        
        return ans