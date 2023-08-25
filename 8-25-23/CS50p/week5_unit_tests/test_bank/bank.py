def main():
    #input from the user(greeting)
    greet = input("Greeting: ")

    #prints the outcome and calls the start function
    print(f"${value(greet)}")

def value(greeting):
    #changed the lower and strip to be applied in the method because when a test is run, python
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()
