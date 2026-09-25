"""this is [LEARNING LOGS] หาจำนวนเฉพาะ"""
def main():
    """this is funct"""
    N = input().split()
    list_num = []
    count = 0
    result = ""

    N1 = int(N[0])
    N2 = int(N[-1])

    for x in range(N1, N2+1):
        c = 0
        for i in range(1, x+1):
            if not x % i:
                c += 1
        if c == 2:
            count += 1
            list_num.append(x)
    for x in list_num:
        if not result:
            result = str(x)
        else:
            result = result + "," + str(x)
    if result:
        print(result)
    print(f"Total primes: {count}")
main()
