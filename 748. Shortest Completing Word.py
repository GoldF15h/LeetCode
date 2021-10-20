def countChr(s,c) :
    op = 0
    for cur in s :
        if cur == c :
            op += 1
    # print('countChr : ',op)
    return op

def isContain(s,d) :
    for cur in d.keys() :
        # print(cur,d[cur],countChr(s,cur))
        if d[cur] > countChr(s,cur) :
            return False
    return True
        
def strToDict(s) :
    d = {}
    for cur in s :
        if cur.isalpha() :
            tmp = cur.lower()
            if d.get(tmp) :
                d[tmp] += 1
            else :
                d.update({tmp:1}) 
    return d

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        d = strToDict(licensePlate)
        ans = '-1'
        for curWord in words :
            if isContain(curWord,d) :
                if ans == '-1' :
                    ans = curWord 
                else :
                    if len(curWord) < len(ans) :
                        ans = curWord
        return ans
                    
        
        
            