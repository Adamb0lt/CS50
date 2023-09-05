import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    #find the time entered by user 1               2               3                  4                  5             6
    if time := re.search(r"([0-1][0-2]|[0-9]|[^[1-9][3-9]]):?([0-5][0-9]|[^[6-9][0-9]])?.{1}(AM|PM).{1}to.{1}([0-1][0-2]|[0-9]|[^[1-9][3-9]]):?([0-5][0-9]|[^[6-9][0-9]])?.{1}(AM|PM)", s):

        #if else statements to check about if AM or PM is entered after the time which will determine the proper range of the hour(0-12 or 12-24)
        if time.group(3) == "AM" and int(time.group(1)) != 12:
            hours1 = int(time.group(1))
        elif time.group(3) == "AM" and int(time.group(1)) == 12:
            hours1 = 0
        elif time.group(3) == "PM" and int(time.group(1)) != 12:
            hours1 = int(time.group(1)) + 12
        if time.group(3) == "PM" and int(time.group(1)) == 12:
            hours1 = int(time.group(1))

        #converting minutes if it exists else it is equal to 0 which will matter for creating the string in the next step
        minutes1 = int(time.group(2)) if time.group(2) else 0

        if time.group(6) == "AM" and int(time.group(4)) != 12:
            hours2 = int(time.group(4))
        elif time.group(6) == "AM" and int(time.group(4)) == 12:
            hours2 = 0
        elif time.group(6) == "PM" and int(time.group(4)) != 12:
            hours2 = int(time.group(4)) + 12
        elif time.group(6) == "PM" and int(time.group(4)) == 12:
            hours2 = int(time.group(4))


        minutes2 = int(time.group(5)) if time.group(5) else 0

        #creates the strings to return to the main function
        if hours1 >= 10 and hours2 >= 10:
            return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
        elif hours1 >= 10 and hours2 < 10:
            return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
        elif hours1 < 10 and hours2 < 10:
            return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
        elif hours1 < 10 and hours2 >= 10:
            return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()

'''
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Modified regular expression to accept both formats
    if time := re.search(r"(\d{1,2})(?::(\d{2}))?\s*(?:AM|PM)\s*to\s*(\d{1,2})(?::(\d{2}))?\s*(?:AM|PM)", s, re.IGNORECASE):
        hours1 = int(time.group(1))
        minutes1 = int(time.group(2)) if time.group(2) else 0
        hours2 = int(time.group(3))
        minutes2 = int(time.group(4)) if time.group(4) else 0

        if 'PM' in s.upper():
            hours1 += 12
            hours2 += 12

        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
    else:
        sys.exit()


if __name__ == "__main__":
    main()'''