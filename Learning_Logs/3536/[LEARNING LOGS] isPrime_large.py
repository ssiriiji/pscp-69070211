"""[LEARNING LOGS] isPrime"""
def main():
    """xxx"""
    n = int(input())

    is_prime = n > 1
    i = 2
    while is_prime and i <= n ** 0.5:
        if not n % i:
            is_prime = False
        i += 1

    if is_prime:
        print("YES")
    else:
        print("NO")
main()
