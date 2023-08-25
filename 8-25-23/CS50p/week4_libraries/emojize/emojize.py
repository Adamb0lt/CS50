#do pip install emoji and then import the emoji package and also requests
import emoji



def main():
    choice = input("Input: ").strip()
    define(choice)

def define(option):
    while True:
        try:#predefined functions in the emoji package 
            print(emoji.emojize(option))
            break
        except(ValueError, NameError):
            pass



if __name__ == "__main__":
    main()