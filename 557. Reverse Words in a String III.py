class Solution:
    def reverseWords(self, s: str) -> str:
        op = []
        for cur in s.split() :
            op.append(cur[::-1])
        return ' '.join(op)