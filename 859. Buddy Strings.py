class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) :
            return False
        
        if sorted(s) != sorted(goal) :
            return False
        
        if s == goal :
            tmp = sorted(s)
            for i in range(len(tmp)-1) :
                if tmp[i] == tmp[i+1] :
                    return True
            return False
        
        count = 0
        for i in range(len(s)) :
            if s[i] != goal[i] :
                count += 1
            if count > 2 :
                return False
        return True