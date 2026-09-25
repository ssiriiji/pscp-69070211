"""this is ไพ่ 44"""
def main():
    """this is code"""
    card = input().upper()
    value = card[:-1]
    suit = card[-1]
    new_type = ""
    new_value = ""
    if suit == "D":
        new_type = "diamonds"
    elif suit == "H":
        new_type = "hearts"
    elif suit == "S":
        new_type = "spades"
    elif suit == "C":
        new_type = "clubs"
    if value == "A":
        new_value = "ace"
    elif value == "J":
        new_value = "jack"
    elif value == "Q":
        new_value = "queen"
    elif value == "K":
        new_value = "king"
    else:
        new_value = value
    print(f"{new_value} of {new_type}")
main()
