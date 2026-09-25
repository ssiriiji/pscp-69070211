"""This is ink"""

import math

def main():
    """This is code"""
    rate, n = map(int, input().split())
    pi = 3.1416
    for _ in range(n):
        x, y = map(int, input().split())
        r2 = x**2 + y**2
        area = pi * r2
        t = area / rate
        print(math.ceil(t))
main()
