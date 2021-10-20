class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        cur = []
        ans = []
        for i in range(len(s)) :
            cur.append(s[i])
            if s[i] == '(' :
                stack.append('(')
            elif s[i] == ')' :
                stack.pop()
            if stack == [] :
                cur.pop(0)
                cur.pop()
                ans += cur
                cur = []
                
        return ''.join(ans)
                