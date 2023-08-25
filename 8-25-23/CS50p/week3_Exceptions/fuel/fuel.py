def main():
    frac = check("Fraction: ")


def check(prompt):
    while True:
        try:
            a,p = input(prompt).split("/")
            t = (int(a) / int(p))
        except (ValueError, ZeroDivisionError):
            print("format is X/Y. Must be less than 1 and greater than 0. X cant be greater than Y")
        else:
            if .99 <= t <= 1:
                print("F\r\n")
            elif t <= .01:
                print("E\r\n")
            elif .01 < t < .99:
                print(f"{t:.0%}\r\n")
            elif t > 1:
                print("X is greater than Y")
                continue #skips current iteration and jumps to next iteration of loop. so it kinda acts as an exception
            break





main()

