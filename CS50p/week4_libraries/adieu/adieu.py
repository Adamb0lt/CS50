#imports
import inflect

p = inflect.engine() #to be used with any inflect specific funtion

def main():
    l = []
    while True:
        try:
            t = input("Name: ").strip().capitalize()
            l.append(t)
        except EOFError:
            break 
    create(l)


def create(li):
    print(f"Adieu, adieu, to {p.join(li)}")




if __name__ == "__main__":
    main()








