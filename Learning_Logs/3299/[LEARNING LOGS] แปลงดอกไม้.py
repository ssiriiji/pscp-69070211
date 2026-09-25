"""[LEARNING LOGS] แปลงดอกไม้"""

thickness, target = map(int, input().split())
planted = 0
strip = 0
while planted < target:
    strip += 1
    cells = thickness * (2 * thickness * strip - thickness + 1) // 2
    planted += cells
print(strip)
