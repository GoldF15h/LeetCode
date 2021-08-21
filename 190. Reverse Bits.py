class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        
        while n > 0 :
            bits.append(n%2)
            n //= 2
        _len = len(bits)
        if _len < 32 :
            bits = bits + [0]*(32-_len)
        # print(bits[::-1])
        # for i in range(32) :
        #     if bits[i] == 0 :
        #         bits[i] = 1
        #     else :
        #         bits[i] = 0
        # print(bits[::-1])
        
        bits = bits[::-1]
        
        op = 0 
        for i in range(32) :
            op += bits[i] * (2**i)
        
        return op