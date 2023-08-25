import random
import sys

def main():
    while True:
        try:
            choice = int(input("Level: ").strip())
            if choice > 0 and choice <= 100:
                rand = random.randint(1,choice)
            else:
                choice/0
        except (ValueError, ZeroDivisionError):
            pass
        else:
            while True:
                try:
                    g = int(input("Guess: ").strip())
                    if g > 0 and g <= choice:
                        if g == rand:
                            print("Just right!")
                            sys.exit()
                        elif g > rand:
                            print("Too large!")
                            g/0
                        elif g < rand:
                            print("Too small!")
                            g/0
                except (ValueError, ZeroDivisionError):
                    pass #Make sure level and guess are integerstry:
main()




















