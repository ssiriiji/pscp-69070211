"""[LEARNING LOGS] Cat and Fox"""
import ast
def main():
    """xxx"""
    n = int(input())
    herd = {}
    for _ in range(n):
        entry = ast.literal_eval(input())
        for name in entry:
            herd[name] = entry[name]
    used_codes = set(herd.values())
    if "Cat01" not in used_codes and "Garfield" not in herd:
        herd["Garfield"] = "Cat01"
    if "Fox01" not in used_codes and "Fubuki" not in herd:
        herd["Fubuki"] = "Fox01"
    cat_list = [(code, name) for name, code in herd.items() if code.startswith("Cat")]
    fox_list = [(code, name) for name, code in herd.items() if code.startswith("Fox")]
    cat_list.sort(key=lambda item: int(item[0][3:]))
    fox_list.sort(key=lambda item: int(item[0][3:]))
    print(f"Cat : {len(cat_list)}")
    print(f"Fox : {len(fox_list)}")
    for code, name in cat_list:
        print(f"{name} : {code}")
    for code, name in fox_list:
        print(f"{name} : {code}")
main()
