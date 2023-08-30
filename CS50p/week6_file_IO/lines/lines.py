import sys


def main():

    #ensures only 1 argument
    if len(sys.argv) == 2:
        print(check(sys.argv[1]))
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def check(arg):
    #for checking if file exists
    try:

        #checks if it ends with py
        if arg.endswith(".py"):

            #counter
            line_count = 0

            #reads lines
            with open(arg, "r") as file: #read is default
                lines = file.readlines()

                #counts lines that aren't comments or are not blank
                for line in lines:
                    if (line.strip().startswith("#") or line.isspace()):
                        pass
                    else:
                        line_count += 1
                return line_count

            #returns file not found or not python file
        else:
            sys.exit("Not a Python File")
    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main()




