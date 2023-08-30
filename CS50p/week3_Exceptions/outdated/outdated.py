# list containing months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
"""accepted = 9/8/1636, September 8, 1636, 9-8-1636
    output - 1636-09-08"""


# main function that calls date
def main():
    date("Date: ")


# date function
def date(prompt):
    while True:
        try:
            # collect input and different scenarios for splitting the input
            today = input("Date: ").capitalize().strip()
            if "/" in today:
                mnth, day, year = today.split(
                    "/"
                )  # TODO: if the slash is placed. have a if or match statement that ensures month is a number, if not reprompt
                if mnth.isalpha():
                    print(not_real)
            elif " " in today:
                mnth, day, year = today.split(
                    " "
                )  # TODO: add an if statement that checks if comma is in day and then do the replace, if not reprompt
                if "," in day and (day[0].isnumeric() or day[1].isnumeric()):
                    day = day.replace(
                        ",", ""
                    )  # TODO: also the same as above but making sure day is only a number, do int() from below if its a string to reprompt
                else:
                    int(Day)
            # formats the month if it is written as text
            if mnth.isalpha() and day.isnumeric() and year.isnumeric():
                if mnth in months:
                    mnth = months.index(mnth) + 1
                day = int(day)
                mnth = int(mnth)
                year = int(year)
            elif mnth.isnumeric() and day.isnumeric() and year.isnumeric():
                day = int(day)
                mnth = int(mnth)
                year = int(year)
            elif (
                mnth.isnumeric() == False
                or year.isnumeric() == False
                or day.isnumeric == False
            ):
                day = int(day)
                mnth = int(mnth)
                year = int(year)

            # ensures that day is between 1 and 31
            if 1 <= day <= 31 and 1 <= mnth <= 12 and 0 <= year <= 9999:
                year = year
            else:
                print(Day)
        except (ValueError, NameError):
            print("format is MM-DD-YYYY or Month DD, YYYY or MM/DD/YY")
        else:
            # final formating for the output in ISO 8601 format
            print(f"{year}-{mnth:02}-{day:02}")
            break


main()
