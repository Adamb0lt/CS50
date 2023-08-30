def main():
    gg = input("Answer to question of life ").lower().replace("-"," ").strip()
    trying(gg)

def trying(p):
    if p == "42" or p == "forty two":
        print("Yes")
    else:
        print("no")

main()

