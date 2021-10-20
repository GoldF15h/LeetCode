class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = list ( sorted(x) for x in words )
        common = []
        for i in range(len(words)-1) :
            a = words[i]
            b = words[i+1]
            # print(a,b)
            curCommon = []
            while len(a) > 0 and len(b) > 0 :
                if a[0] == b[0] :
                    curCommon.append(a[0])
                    a.pop(0)
                    b.pop(0)
                elif a[0] < b[0] :
                    a.pop(0)
                else :
                    b.pop(0)
            words[i+1] = curCommon
            # print("curCommon =",curCommon)
        return words[-1]
                    