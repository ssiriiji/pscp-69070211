"""[LEARNING LOGS] Among Us"""
import ast

def main():
    """xxx"""
    alive = {}
    while True:
        line = input()
        if line == "Start":
            break
        alive.update(ast.literal_eval(line))

    dead = {}
    while True:
        name = input()
        if name == "End":
            break
        if name in alive:
            dead[name] = alive.pop(name)

    impostors = list(alive.values()).count("Impostor")

    print(impostors, "Impostor Remains")
    print("***Alive***")
    for name, role in sorted(alive.items()):
        print(name, ":", role)
    print("***Dead***")
    for name, role in sorted(dead.items()):
        print(name, ":", role)
main()
