"""[LEARNING LOGS] Tile Knocking Robot"""
def main():
    """xxx"""
    n, p = input().split()
    n = int(n)
    p = float(p)

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0

    for row in grid:
        row_tiles = 0
        row_points = 0
        for j in range(n):
            if row[j] > 0:
                row_tiles += 1
                col_tiles[j] += 1
            row_points += row[j]
            col_points[j] += row[j]
        print(*row, row_tiles, row_points)
        total_tiles += row_tiles
        total_points += row_points

    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
