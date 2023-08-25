menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    choice = choose("Item: ")

def choose(prompt):
    c = 0
    while True:
        try:
            a = input("Item: ").lower().strip()
            a = a.split(" ")
            if len(a) > 1:
                c += float(menu[a[0].capitalize()+" " +a[1].capitalize()])
            elif len(a) == 1:
                c += float(menu[a[0].capitalize()])
        except (ValueError,KeyError):
            print("item is not on the menu ")
        except EOFError:
            print("\n")
            break
        else:
            print(f"Total: ${c:.2f}")

main()





