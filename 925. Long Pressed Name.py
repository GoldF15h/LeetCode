def sol (name: str, typed: str) :
    # print(name,typed)
    i = 0
    j = 0
    nameStack = []
    typedStack = []
    while True :
        nameStack = []
        typedStack = []
        # print('****************\n',i,j,'\n\nin name')
        if i < len(name) :
            cur = name[i]
        while i < len(name) and name[i] == cur :
            # print(i,cur,name[i])
            nameStack.append(name[i])
            i += 1

        # print('\nin typed')
        if j < len(typed) :
            cur = typed[j]
        while j < len(typed)and typed[j] == cur  :
            # print(j,cur,typed[j])
            typedStack.append(typed[j])
            j += 1
        
        # print('\ncheck stack',nameStack,'\nand        ',typedStack)
        if nameStack == [] or typedStack == [] :
            return False
        if nameStack[0] != typedStack[0] :
            return False
        if len(nameStack) > len(typedStack) :
            return False
        if i == len(name) and j == len(typed) :
            return True


if __name__ == "__main__" :
    a = input().strip('"')
    b = input().strip('"')
    print(sol(a,b))