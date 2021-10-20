class Solution:
    def tribonacci(self, n: int) -> int:
        dy = [0,1,1]
        if n < 3 :
            return dy[n]
        for i in range(n-2) :
            dy.append( dy[-1] + dy[-2] + dy[-3] )
        # print(dy)
        return dy[-1]