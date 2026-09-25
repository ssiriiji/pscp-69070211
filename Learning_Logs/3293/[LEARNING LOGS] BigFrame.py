"""[LEARNING LOGS] BigFrame"""

lines = [input().rstrip() for _ in range(5)]
width = max(len(s) for s in lines)
border = "*" * (width + 4)
print(border)
for line in lines:
    print("* " + line.ljust(width) + " *")
print(border)
