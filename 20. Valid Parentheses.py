def sol (s) :
    stack = []
    tail = -1
    for cur in s :
        if cur in ['{','(','['] :
            stack.append(cur)
            tail = tail + 1
        if cur in ['}',')',']'] :

            if tail == -1 :
                return False

            if stack[tail] == '{' and cur == '}':
                stack.pop()

            elif stack[tail] == '(' and cur == ')':
                stack.pop()

            elif stack[tail] == '[' and cur == ']':
                stack.pop()
            
            else :
                return False
            tail = tail - 1

    if tail == -1 :
        return True
    else :
        return False

if __name__ == "__main__" :
    inp = input().strip('"')
    print(sol(inp))