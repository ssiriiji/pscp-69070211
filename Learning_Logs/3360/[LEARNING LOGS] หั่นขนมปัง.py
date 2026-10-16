"""[LEARNING LOGS] Bread"""
def main():
    """xxx"""
    w, h, _, _ = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    xs = [0] + xs + [w]
    ys = [0] + ys + [h]

    widths = []
    for i in range(1, len(xs)):
        widths.append(xs[i] - xs[i - 1])

    heights = []
    for i in range(1, len(ys)):
        heights.append(ys[i] - ys[i - 1])

    widths.sort(reverse=True)
    heights.sort(reverse=True)

    first = widths[0] * heights[0]

    candidates = []
    if len(widths) > 1:
        candidates.append(widths[1] * heights[0])
    if len(heights) > 1:
        candidates.append(widths[0] * heights[1])

    second = max(candidates)
    print(first, second)
main()
