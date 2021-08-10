ladder_data = [1,2] + [-1]*100

def ladder (n) :
    # print(ladder_data[n-1])
    if ladder_data[n-1] == -1 :
        ladder_data[n-1] = ladder(n-1) + ladder(n-2)
        return ladder_data[n-1]
    else :
        return ladder_data[n-1]

def sol(n) :
    return ladder(n)

if __name__ == "__main__" :
    x = int(input())
    print(sol(x))