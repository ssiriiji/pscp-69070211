"""[LEARNING LOGS] Pad Thai"""
def main():
    """xxx"""
    recipe = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
              "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg",
              "Oil", "Peanuts"}
    target_taste = {"Sweet", "Sour", "Salty"}

    used = set()
    while True:
        item = input()
        if item == "Cook":
            break
        used.add(item)

    taste = set()
    while True:
        item = input()
        if item == "End":
            break
        taste.add(item)

    if not used.issubset(recipe):
        print("This is not Pad Thai!!!")
    elif used != recipe:
        print("This is bad!")
    elif taste == target_taste:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
