def sol (a,b) :
    # a always longer than b
    if len(a) < len(b) :
        a,b = b,a

    # make len(b) = len(a)
    b = ( "0"*(len(a)-len(b)) ) + b

    # rev a and b
    a = a[::-1]
    b = b[::-1]

    # calculate
    op = ""
    _c = 0
    while a != '' and b != '' :
        # print( a," AND ", b)
        _a = int(a[0])
        _b = int(b[0])

        if ( _a + _b + _c ) % 2 == 1 :
            op = op + '1' 
        else :
            op = op + '0'
        
        _c = ( _a + _b + _c  ) // 2
        a = a[1::]
        b = b[1::]

    # check for last carrier
    if _c == 1 :
        op = op + '1'

    # rev op
    op = op[::-1]

    # return
    return op

if __name__ == "__main__" :
    a = input().strip('"')
    b = input().strip('"')
    print(sol(a,b))