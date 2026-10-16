"""[LEARNING LOGS] Shorten"""
def main():
    """xxx"""
    nums = []
    while True:
        num = int(input())

        if num == -1:
            break
        nums.append(num)

    result = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if i == j:
            result.append(str(nums[i]))
        else:
            result.append(f"{nums[i]}-{nums[j]}")
        i = j + 1

    print(", ".join(result))
main()
