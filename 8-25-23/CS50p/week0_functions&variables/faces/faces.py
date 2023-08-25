def convert(lol):
    lol1 = lol.replace(":)","🙂")
    lol2 = lol1.replace(":(","🙁")
    return lol2


def main():
    lol = input(" ")
    gg = convert(lol)
    print(gg)





main()

