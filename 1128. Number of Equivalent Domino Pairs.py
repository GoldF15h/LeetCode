class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)) :
            if dominoes[i][0] > dominoes[i][1] :
                dominoes[i][0],dominoes[i][1] = dominoes[i][1],dominoes[i][0]
        dominoes.sort()
        ans = 0
        
        print(dominoes)
        
        i = 0
        while i < len(dominoes)-1 :
            if dominoes[i] == dominoes[i+1] :
                # print(dominoes[i])
                cur = dominoes[i]
                n = 1
                while i < len(dominoes)-1 and dominoes[i+1] == cur :
                    n += 1
                    i += 1
                # print(n)
                n -= 1
                while n > 0 :
                    ans += n
                    n -= 1
            i += 1
        
        return ans