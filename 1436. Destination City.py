class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for start,stop in paths :
            if d.get(start) :
                d[start] = stop
            else :
                d.update({start:stop})
        cur = paths[0][0]
        while d.get(cur) :
            cur = d[cur]
        return cur
                
        