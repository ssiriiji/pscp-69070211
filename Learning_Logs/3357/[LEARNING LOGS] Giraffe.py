"""[LEARNING LOGS] Giraffe"""
def main():
    """xxx"""
    n = int(input())
    heights = []
    for _ in range(n):
        heights.append(int(input()))

    count = 0
    for i in range(n):
        left_ok = (not i) or (heights[i] > heights[i - 1])
        right_ok = (i == n - 1) or (heights[i] > heights[i + 1])

        if left_ok and right_ok:
            count += 1
    print(count)
main()
