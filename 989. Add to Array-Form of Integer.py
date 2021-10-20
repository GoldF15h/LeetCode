class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        cur = k
        ans = []
        for i in range(len(num)) :
            cur += num[i] * (10**i)
        if cur != 0 :
            while cur > 0 :
                ans.append(cur%10)
                cur //= 10
        else :
            ans = [0]
        return ans[::-1]
        