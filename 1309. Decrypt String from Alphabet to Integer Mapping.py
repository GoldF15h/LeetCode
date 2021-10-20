class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # print(alp)
        for i in range(len(s)) :
            if s[i] == '#' :
                tmp = stack[-2]*10 + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            else :
                stack.append(int(s[i]))
        ans = ''
        for cur in stack :
            ans += alp[cur-1]
        return ans