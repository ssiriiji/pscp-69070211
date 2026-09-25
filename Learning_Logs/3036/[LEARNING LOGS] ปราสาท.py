"""This is ปราสาท"""
import math

def main():
    """This is code"""
    n = int(input())

    if n == 1:
        print(0)
    else:
        ring = math.ceil(math.sqrt(n))
        pos = n - (ring - 1) ** 2
        if pos % 2:
            print(2 * (ring - 1))
        else:
            print(2 * (ring - 1) - 1)
main()
