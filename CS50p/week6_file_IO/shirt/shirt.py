import sys

# needed for opening the file and also sizing the images properly
from PIL import Image, ImageOps


def main():
    # ensures only 2 argument
    if len(sys.argv) == 3:
        # formats
        forms = ["jpeg", "jpg", "png"]
        arg1, ending1 = sys.argv[1].split(".")
        arg2, ending2 = sys.argv[2].split(".")

        # checks for correct input and output file extenstions
        if ending1 in forms:
            if ending1 == ending2:
                create(sys.argv[1], sys.argv[2])
            # two elses that exit given either different extenstions or input extension is wrong
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def create(arg1, arg2):
    try:
        # opens and create variables to represent the images
        shirt = Image.open("shirt.png")
        arg1 = Image.open(arg1)

        # make arg1 fit to size of shirt and then pastes the image to save
        new_image = ImageOps.fit(arg1, shirt.size)
        new_image.paste(shirt, mask=shirt)
        new_image.save(arg2)

    except FileNotFoundError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
