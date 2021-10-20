class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        for i in range(1,n+1) :
            # print(i)
            if j < len(target) :
                if target[j] != i :
                    ans += ["Push","Pop"]
                else :
                    ans += ["Push"]
                    j += 1
                
            else :
                break 
        return ans
            