def sol (x) :
    x = str(x) 
    return True if x == x[::-1] else False

if __name__ == "__main__" :
    x = int(input)
    print(sol(x))