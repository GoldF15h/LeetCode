class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        
        s1d = {}
        for cur in s1.split() :
            if s1d.get(cur) :
                s1d[cur] += 1
            else :
                s1d.update({cur:1})
        s2d = {}
        for cur in s2.split() :
            if s2d.get(cur) :
                s2d[cur] += 1
            else :
                s2d.update({cur:1})
                
        s1key = list(s1d.keys())
        s2key = list(s2d.keys())
        for cur in s1key :
            if cur in s2key :
                s1d.pop(cur)
                s2d.pop(cur)
                
        s1key = list(s1d.keys())
        s2key = list(s2d.keys())
        for cur in s2key :
            if cur in s1key :
                s1d.pop(cur)
                s2d.pop(cur)
            
        l = list(s1d.keys())
        for cur in l :
            if s1d[cur] > 1 :
                s1d.pop(cur)
        l = list(s2d.keys())
        for cur in l :
            if s2d[cur] > 1 :
                s2d.pop(cur)
        
        d = {}
        fi = list(s1d.keys()) + list(s2d.keys())
        for cur in fi :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        for cur in d.keys() :
            if d[cur] == 1 :
                ans.append(cur)
        
        return ans