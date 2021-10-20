class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1,n+1) :
            sumDig = 0
            tmp = i
            while tmp > 0 :
                sumDig += tmp%10
                tmp //=10
            if d.get(sumDig) :
                d[sumDig] += 1
            else :
                d.update({sumDig:1})
        _max = max(list(d.values()))
        ans = 0
        for cur in d.keys() :
            if d[cur] == _max :
                ans += 1
        return ans