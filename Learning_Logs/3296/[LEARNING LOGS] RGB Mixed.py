"""[LEARNING LOGS] RGB Mixed"""

r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())
r = (r1 + r2) // 2
g = (g1 + g2) // 2
b = (b1 + b2) // 2
print(r, g, b)
