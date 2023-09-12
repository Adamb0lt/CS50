from datetime import date
import sys
import re
import inflect
import operator

p = inflect.engine()

def main():
    # ask for DOB
    dia = input("Date of Birth: ").strip()

    #operator class with overloading through __sub__ or sub in this case that allows for subtraction of the functions/objects
    diff = operator.sub(date.today(), translate(dia))


    diff = diff.days * 1440 #.days changes it from datetime.delta to an int
    print(f"{p.number_to_words(diff, andword='').capitalize()} minutes")


def translate(d):
    try:
        #searches for date format
        if check := re.search(r'^\d{4}-\d{2}-\d{2}$', d):

            #returns date in date(year, month, day) and also checks that month is 1-12, day is 1-31. If not its a ValueError
            return date.fromisoformat(d)
        else:
            raise ValueError("Invalid date")
    except ValueError:
        sys.exit("Invalid date")




if __name__ == "__main__":
    main()