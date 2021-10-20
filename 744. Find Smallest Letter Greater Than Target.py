class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ord = ord(target)
        i = 0
        jump = 1
        _len = len(letters)
        while i < _len :
            if ord(letters[i]) > target_ord :
                return letters[i]
            if i + jump < _len and ord(letters[i+jump]) <= target_ord :
                i += jump
                jump *= 2
            else :
                i += 1
                jump = 2
        return letters[0]