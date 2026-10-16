"""[LEARNING LOGS] Forward Message"""
def main():
    """xxx"""
    n, s = map(int, input().split())
    forward = [0]
    for _ in range(n):
        forward.append(int(input()))

    received = set()
    current = s
    while current and current not in received:
        received.add(current)
        current = forward[current]

    print(len(received))
main()
