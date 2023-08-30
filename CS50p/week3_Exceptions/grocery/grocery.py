def main():
    # calls choose function
    choose("")


def choose(choice):
    # empty dictionary and count variable for appearance of each item
    l = {}
    count = 1
    try:
        while True:
            # input
            food = input("").strip().upper()

            # if else statement that places input into dictionary and also updates count on it if its repeated
            if food in l.keys():
                l[food] += 1
            else:
                l[food] = count
    # except EOF that acts as the final piece for ending the program with ctrl+d and prints summary of all items
    except EOFError:
        print("\n")
        p = sorted(l.keys())
        for i in p:
            if i in l:
                print(f"{l[i]} {i}")


# call main function
main()
