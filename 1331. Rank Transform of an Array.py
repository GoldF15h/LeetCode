class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        l = list(set(arr))
        l.sort()
        for i in range(len(l)) :
            d.update({l[i]:i+1})
        for i in range(len(arr)) :
            arr[i] = d[arr[i]]
        return arr
