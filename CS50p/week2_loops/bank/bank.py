def main():
    #input from the user(greeting)
    greet = input("Greeting: ").lower().strip()

    #prints the outcome and calls the start function
    print(f"${start(greet)}")

def start(p):
    #
    if "hello" in p:
        return 0
    elif "h" in p[0]:
        return 20
    else:
        return 100

main()
