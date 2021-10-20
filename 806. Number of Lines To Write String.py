class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        curLine = 0
        totalLines = 0
        for cur in s :
            
            if curLine + widths[ord(cur)-ord('a')] <= 100 :
                curLine += widths[ord(cur)-ord('a')]
            else :
                curLine = widths[ord(cur)-ord('a')]
                totalLines += 1
            # print(cur,curLine,totalLines)
        return [totalLines+1,curLine]