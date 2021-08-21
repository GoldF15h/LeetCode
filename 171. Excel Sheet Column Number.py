def sol (columnTitle) :
    _pow = len(columnTitle) - 1 
    op = 0
    for i in columnTitle :
        # print( i , ( ord(i) - ord('A') + 1 ) , ( 26 ** _pow ) )
        op +=  ( ord(i) - ord('A') + 1 ) * ( 26 ** _pow )
        _pow -= 1
    return op

if __name__ == '__main__' :
    s = input()
    print(sol(s))