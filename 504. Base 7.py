class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0 :
            return '0'
        op = ''
        if num >= 0 :
            isMinus = False
        else :
            num *= -1
            isMinus = True
        while num > 0 :
            op += str(num%7)
            num //= 7
        if isMinus :
            return '-'+op[::-1]
        else :
            return op[::-1]