def sol(num) :
    _min = 2**31
    if num == 0 :
        return '0'
    bits = []
    final_dig = 0 if num > 0 else 1
    if num < 0 :
        num = _min + num
    while num > 0 :
        bits.append(num%2)
        num//=2
    bits = bits + [0]*(31-len(bits)) +[final_dig]
    bits = bits[::-1]
    op = ''
    hex_set = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(0,32,4) :
        cur = bits[i:i+4:]
        _sum = 8*cur[0] + 4*cur[1] + 2*cur[2] + 1*cur[3]
        op += hex_set[_sum]
    if final_dig :
        return op
    else :
        for i in range(8) :
            if op[0] == '0' :
                op = op[1::]
            else :
                return op

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))