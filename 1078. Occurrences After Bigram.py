class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = text.split()
        ans = []
        for i in range(len(l)-2) :
            if l[i] == first and l[i+1] == second :
                ans.append(l[i+2])
        return ans