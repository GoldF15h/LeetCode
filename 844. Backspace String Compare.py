def backSpaceProcess(s) :
    stack = []
    for i in range(len(s)) :
        if s[i] != '#' :
            stack.append(s[i])
        else :
            if stack != [] :
                stack.pop()
    return ''.join(stack)

def sol (s,t) :
    return backSpaceProcess(s) == backSpaceProcess(t)

if __name__ == "__main__" :
    s = input().strip('"')
    t = input().strip('"')
    print(sol(s,t))