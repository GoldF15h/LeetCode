class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for cur in arr :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        
        l = list(d.values())
        return len(l) == len(set(l))