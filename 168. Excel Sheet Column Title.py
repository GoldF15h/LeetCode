def sol (columnNumber) :
    stack = []
    while columnNumber > 0 :
        tmp = columnNumber % 26
        if tmp == 0 :
            stack.append( 'Z' )
            columnNumber -= 26
        else :
            stack.append( chr( ord('A') + tmp - 1 ) )
        columnNumber //= 26
    return ''.join(stack[::-1])
    
if __name__ == "__main__" :
    n = int(input())
    # for n in range(100) :
    print('case #{} -> {}'.format(n,sol(n)))