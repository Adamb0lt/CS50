import re
import sys

def main():
    print(validate(input("IPV4 Address: ")))

def validate(ip):
    ip = ip.strip()

    #looks for number between 0 and 255 for each octet and also ensures that there must be a dot after each number
    #pairing of brackets creates range with in the tens example [0-9][0-9] = 0-99. Cant go further
    if check := re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()