"""this is [LEARNING LOGS] BrickBridge"""
def main():
    """this is code"""
    a = int(input())
    b = int(input())
    goal = int(input())

    sum_b = goal // 5

    if b >= sum_b:
        max_big = sum_b
    else:
        max_big = sum_b

    new_goal = goal - max_big * 5

    if new_goal <= a:
        print(new_goal)
    else:
        print(-1)
main()
