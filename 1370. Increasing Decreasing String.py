class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for cur in s :
            if d.get(cur) :
                d[cur] += 1
            else :
                d.update({cur:1})
        # print(d)
        l = list(d.keys())
        l.sort()
        ans = ''
        revL = l[::-1]
        while len(ans) < len(s) :
            for cur in l :
                if d[cur] > 0 :
                    ans += cur
                    d[cur] -= 1
            for cur in revL :
                if d[cur] > 0 :
                    ans += cur
                    d[cur] -= 1
        return ans
        