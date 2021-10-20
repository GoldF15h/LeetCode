class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)) :
            mat[i] = sum(mat[i])
        l = sorted(list(set(mat)))
        ans = []
        for cur in l :
            for i in range(len(mat)) :
                if mat[i] == cur :
                    ans.append(i)
                    if len(ans) == k :
                        return ans