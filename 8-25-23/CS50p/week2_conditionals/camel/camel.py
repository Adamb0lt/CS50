def main():
    name = input("variable name in camelCase: ").strip()
    adjust(name)

def adjust(llame):
    for i in llame:
        if i.isupper():
            print("_" + i.lower(),end = "")
        else:
            print(i,end="")
    print("\n")

main()


#converts from snake case to camel case
'''def main():
    name = input("variable name in camelCase: ").strip()
    name = name.lower()
    name = name.split("_")
    adjust(name)

def adjust(llame):
    for i in llame:
        if i == llame[0]:
            print(i, end="")
        elif i != llame[0]:
            print(i.capitalize(), end="")

    print("new line")

main()'''

