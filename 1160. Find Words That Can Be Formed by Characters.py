class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chDict = {}
        ans = 0
        for cur in chars :
            if chDict.get(cur) :
                chDict[cur] += 1
            else :
                chDict.update({cur:1})
        
        for curWord in words :
            tmpDict = chDict.copy()
            curAdd = len(curWord)
            for curChr in curWord :
                # print(tmpDict)
                if tmpDict.get(curChr) :
                    if tmpDict[curChr] <= 0 :
                        # print('break!',curWord)
                        curAdd = 0
                        break
                    else :
                        tmpDict[curChr] -= 1
                else :
                    curAdd = 0
                    break
            ans += curAdd
        return ans