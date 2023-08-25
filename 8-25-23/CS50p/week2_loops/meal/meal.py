def main():
    time = input("Time? ").strip()

    #
    num = convert(time)
    if 7 <= num <= 8:
        print("breakfast time")
    elif 12 <= num <= 13:
        print("lunch time")
    elif 18 <= num <= 19:
        print("dinner time")


def convert(p):
    hours, minutes = p.split(":")
    num = float(hours)+ float(minutes)/60
    return num



if __name__ == "__main__":
    main()
# old code for convert that works but not how CS50 wants it
""" def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if 0 <= hours < 12 and 0 <= minutes < 60:
        print("breakfast time")
    elif 12 <= hours < 18 and 0 <= minutes < 60:
        print("lunch time")
    elif 18 <= hours < 24 and 0 <= minutes < 60:
        print("dinner time")"""




