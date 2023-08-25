def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalpha() and s.isupper():
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
    #else statement for 1st if
    else:
        return False



















'''
#this is_valid doesnt work because input/string from main function is immutable when in the is_valid function
def is_valid(s):
    # must be between 2 and 6 characters and start with letter
    # solves for if all characters are letters and is between 2 and 6 characters. Done
    if 2 <= len(s) <= 6 and s.isalpha() and s.isupper():
        return True
    elif 2 <= len(s) <= 6 and s[0].isalpha() and s.isspace() == False and s.isupper():
        #index of first number in the string
        ss = s
        for i in s:
            if i.isdigit() == True and i != "0":
                newS.replace(i,"*")
            elif i.isdigit() == True and i == "0":
                newS.replace(i,"-")
        p = s.find("*")
        if s[p] == "-":
            return False
        else:
        # variable for tracking up to the last character of the string
        # checks if len(s) is greater than first location of number
            while len(s)-(p+1)>= 0:
                if s[p] == "*" or s[p] == "-":
                    p += p
                elif s[p] != "*" or s[p-1] != "-":
                    return False
            return True
#else statement for first if statement
    else:
        return False '''

main()

