def main():
    frac = gauge(convert("Fraction: "))


def convert(prompt):
    while True:
        try:
            a,p = input(prompt).split("/")
            t = int(a) / int(p)
            if 0 < t < 1:
                t = t * 100
                return int(t)
            elif 0 > t > 1:
                raise ValueError("Fraction is greater than 1 or less than 0")
        except (ValueError, ZeroDivisionError, TypeError):
            print("format is X/Y. Must be less than 1 and greater than 0. X cant be greater than Y")





def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()

