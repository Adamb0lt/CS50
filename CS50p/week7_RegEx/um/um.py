import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = " " + s + " "
    cnt = 0
    if check := re.findall(r"\bum\b",s,flags = re.IGNORECASE):
        for i in check:
            cnt += 1
        return cnt







if __name__ == "__main__":
    main()