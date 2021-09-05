class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = { 'U':0,'D':0,'L':0,'R':0 }
        for cur in moves :
            d[cur] += 1
        if d['U'] == d['D'] and d['R'] == d['L'] :
            return True
        return False