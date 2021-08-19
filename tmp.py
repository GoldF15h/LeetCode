columnNumber = int(input())

stack = []
while columnNumber > 0:
    remain = columnNumber % 26
    stack.append(chr(ord('A') + remain - 1) if remain else 'Z')
    if not remain: 
        columnNumber -= 26
    columnNumber //= 26
print(stack)