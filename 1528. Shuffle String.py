class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = '_'*len(s)
        ans = list(ans)
        for i in range(len(s)) :
            ans[indices[i]] = s[i]
        return ''.join(ans)