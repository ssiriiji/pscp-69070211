"""[LEARNING LOGS] B - Fully"""
def main():
    """xxx"""
    text = input()

    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    result = ""
    for ch, count in counts.items():
        if count % 2 == 1:
            result += ch

    if result:
        print(result)
    else:
        print("fully paired")
main()
