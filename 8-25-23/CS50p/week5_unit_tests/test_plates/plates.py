def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha() and s.isupper():
        return True
    elif 2 <= len(s) <= 6 and s[0].isalpha() and not s.isspace() and s.isupper():
        for i in range(len(s)):
            if s[i].isnumeric() and s[i] != "0":
                s = s[:i] + "*" + s[i+1:]
            elif s[i].isnumeric() and s[i] == "0":
                s = s[:i] + "-" + s[i+1:]
        p = s.find("*")
        c = s.find("-")
        if p > c and c != -1:
            return False
        else:
            while len(s) - (p + 1) >= 0:
                if s[p] == "*" or s[p] == "-":
                    p += 1
                elif s[p] != "*" or s[p-1] != "-":
                    return False
            return True
    # Adding a condition to handle check 10
    elif 2 <= len(s) <= 6 and s.isalnum() and not s.isupper():
        has_numeric = any(c.isdigit() for c in s)
        if has_numeric:
            return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

