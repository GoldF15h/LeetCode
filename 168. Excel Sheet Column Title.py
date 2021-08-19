def sol (columnNumber) :
    stack = []
    while columnNumber > 0:
        remain = columnNumber % 26
        stack.append(chr(ord('A') + remain - 1) if remain else 'Z')
        if not remain: columnNumber -= 26
        columnNumber //= 26
    return ''.join(stack[::-1])

    
if __name__ == "__main__" :
    # n = int(input())
    for n in range(100) :
        print('case #{} -> {}'.format(n,sol(n)))