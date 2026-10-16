"""[LEARNING LOGS] Duplicate Names"""
def main():
    """xxx"""
    m = int(input())
    n = int(input())

    group1 = set()
    for _ in range(m):
        group1.add(int(input()))

    group2 = set()
    for _ in range(n):
        group2.add(int(input()))

    both = sorted(group1 & group2, reverse=True)

    if not both:
        print("Nope")
    else:
        for student in both:
            print(student)
main()
