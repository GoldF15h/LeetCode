class Solution:
    def checkRecord(self, s: str) -> bool:
        aCount = 0
        lCount = 0
        for cur in s :
            if cur == 'A' :
                aCount += 1
                if aCount == 2:
                    return False
                lCount = 0
            if cur == 'L' :
                lCount += 1
                if lCount == 3 :
                    return False
            if cur == 'P' :
                lCount = 0
        return True
        