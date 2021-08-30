def toDec (n) :
    n = n[::-1]
    op = 0
    for i in range(len(n)) :
        op += n[i]*(2**i)
    return op

def toBi (n) :
    op = []
    while n > 0 :
        op.append(n%2)
        n //= 2
    return op[::-1]

def sol (num) :
    bits = toBi(num)
    for i in range(len(bits)) :
        bits[i] = 1 if bits[i] == 0 else 0
    return toDec(bits)

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))